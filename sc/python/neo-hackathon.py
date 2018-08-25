from boa.interop.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import *
from boa.interop.Neo.Transaction import Transaction, GetReferences, GetOutputs, GetUnspentCoins
from boa.interop.Neo.Output import GetValue, GetAssetId, GetScriptHash
from boa.interop.Neo.Blockchain import GetHeight
from nep5.token import *


TOKENS_PER_NEO = 10 * 100000000

NEO_ASSET_ID = b'\x9b|\xff\xda\xa6t\xbe\xae\x0f\x93\x0e\xbe`\x85\xaf\x90\x93\xe5\xfeV\xb3J\\"\x0c\xcd\xcfn\xfc3o\xc5'

GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'

OnTransfer = RegisterAction('transfer', 'addr_from', 'addr_to', 'amount')

ctx = GetContext()


def Main(operation, args):
    trigger = GetTrigger()

    if trigger == Verification():
        if CheckWitness(OWNER):
            return True

        return False

    elif trigger == Application():
        for op in NEP5_METHODS:
            if operation == op:
                return handle_token(ctx, operation, args)

        if operation == 'deploy':
            return deploy()

        elif operation == 'claimTokens':
            return claim_tokens(ctx)

        elif operation == 'availableAmount':
            return available_amount(ctx)

        return 'unknown operation'

def deploy():
    if not CheckWitness(OWNER):
        print("Must be owner to deploy")
        return False

    if not Get(ctx, 'initialized'):
        Put(ctx, 'initialized', 1)
        Put(ctx, OWNER, INITIAL_AMOUNT)
        return True

    return False


def claim_tokens(ctx):
    attachments = get_asset_attachments()  # [receiver, sender, neo, gas]

    current_balance = Get(ctx, attachments[1])
    if current_balance > 0:
        return False
    amount = attachments[2] * TOKENS_PER_NEO / 100000000
    new_balance = current_balance + amount
    Put(ctx, attachments[1], new_balance)

    OnTransfer(attachments[0], attachments[1], amount)

    return True


def available_amount(ctx):
    total_supply = Get(ctx, TOTAL_SUPPLY_KEY)
    return TOTAL_SUPPLY_CAP - total_supply


# ################################################
# Helper
# ################################################

def get_asset_attachments():
    tx = GetScriptContainer()
    references = tx.References

    receiver_addr = GetExecutingScriptHash()
    sender_addr = None
    sent_amount_neo = 0
    sent_amount_gas = 0

    if len(references) > 0:
        reference = references[0]
        sender_addr = reference.ScriptHash
        for output in tx.Outputs:
            if output.ScriptHash == receiver_addr:
                if output.AssetId == NEO_ASSET_ID:
                    sent_amount_neo += output.Value
                if output.AssetId == GAS_ASSET_ID:
                    sent_amount_gas += output.Value

    return [receiver_addr, sender_addr, sent_amount_neo, sent_amount_gas]

