from boa.interop.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.interop.Neo.Runtime import *
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import *
from boa.interop.Neo.Transaction import Transaction, GetReferences, GetOutputs, GetUnspentCoins
from boa.interop.Neo.Output import GetValue, GetAssetId, GetScriptHash
from boa.interop.Neo.Blockchain import GetHeight
from boa.builtins import *
from nep5.token import *

BOOKLIST = b'book_list'

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
            return deploy(ctx)

        elif operation == 'claimTokens':
            return claim_tokens(ctx)

        elif operation == 'vote':
            if len(args) == 2:
                return vote(ctx, args[0], args[1])

        elif operation == 'getVote':
            if len(args) == 1:
                return get_vote(ctx, args[0])

        elif operation == 'getData':
            return get_data(ctx)

        elif operation == 'putData':
            if len(args) == 1:
                return put_data(ctx, args[0])

        elif operation == 'deleteData':
            return delete_data(ctx)

        elif operation == 'withdraw':
            if len(args) == 1:
                return withdraw(ctx, args[0])

        return 'unknown operation'

def deploy():
    if not CheckWitness(OWNER):
        print("Must be owner to deploy")
        return False

    if not Get(ctx, 'initialized'):
        Put(ctx, 'initialized', 1)
        Put(ctx, OWNER, TOTAL_SUPPLY_CAP)
        return True

    return False

def claim_tokens(ctx):
    attachments = get_asset_attachments()  # [receiver, sender, neo, gas]

    current_balance = Get(ctx, attachments[1])
    if current_balance > 0:
        return False
    amount = 1
    new_balance = current_balance + amount
    Put(ctx, attachments[1], new_balance)

    OnTransfer(attachments[0], attachments[1], amount)

    return True

def vote(ctx, bhash, address):
    attachments = get_asset_attachments()  # [receiver, sender, neo, gas]

    Notify(bhash)
    Notify(address)

    if Get(ctx, concat(bhash, concat(b'-', attachments[1]))) != 0:
        return False

    put_vote(ctx, bhash, address)

    Put(ctx, concat(bhash, concat(b'-', attachments[1])), 1)

    return True

def get_vote(ctx, bhash):
    return Get(ctx, bhash)

def put_vote(ctx, bhash, address):
    vote_data = Get(ctx, bhash)
    if len(vote_data) != 0:
        vote_dict = Deserialize(vote_data)
    else:
        vote_dict = {}
    if has_key(vote_dict, address):
        vote_dict[address] += 1
    else:
        vote_dict[address] = 1
    Put(ctx, bhash, Serialize(vote_dict))
    return True

def withdraw(ctx, bhash):
    Notify(bhash)
    attachments = get_asset_attachments()
    vote_data = Get(ctx, bhash)
    if len(vote_data) != 0:
        vote_dict = Deserialize(Get(ctx, bhash))
    else:
        return False
    raddress = reliable_address(vote_dict)
    vote_count = vote_dict[raddress]
    Notify(raddress)
    Notify(attachments[1])
    Notify(vote_count)
    if raddress == attachments[1] and vote_count > 0:
        transfer(ctx, OWNER, raddress, 100)
        return True
    return False

def get_data(ctx):
    return Get(ctx, BOOKLIST)


def put_data(ctx, data):
    book_list = Get(ctx, BOOKLIST)
    if len(book_list) == 0:
        Put(ctx, BOOKLIST, data)
        return True
    result = concat(book_list, concat(b',', data))
    Put(ctx, BOOKLIST, result)
    return True

def delete_data(ctx):
    Delete(ctx, BOOKLIST)
    return True


# ################################################
# Helper
# ################################################

def reliable_address(vdict):
    max_reliable = 0
    address = ''
    for i in keys(vdict):
        if vdict[i] > max_reliable:
            max_reliable = vdict[i]
            address = i
    return address

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
