from boa.interop.Neo.Runtime import CheckWitness, Notify
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Storage import *
from boa.builtins import concat


NAME = 'SanchoCoin'

SYMBOL = 'SAN'

DECIMALS = 8

OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'

NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer']

TOTAL_SUPPLY_KEY = b'total_supply'

TOTAL_SUPPLY_CAP = 1000000 * 100000000

OnTransfer = RegisterAction('transfer', 'addr_from', 'addr_to', 'amount')

def handle_token(ctx, operation, args):

    if operation == 'name':
        return NAME

    elif operation == 'symbol':
        return SYMBOL

    elif operation == 'decimals':
        return DECIMALS

    elif operation == 'balanceOf':
        if len(args) == 1:
            return Get(ctx, args[0])

    elif operation == 'totalSupply':
        return Get(ctx, TOTAL_SUPPLY_KEY)


    elif operation == 'transfer':
        if len(args) == 3:
            return transfer(ctx, args[0], args[1], args[2])

    print("invalid args")
    return False


def transfer(ctx, from_addr, to_addr, amount):
    if amount <= 0:
        return False

    if len(to_addr) != 20:
        return False

    if CheckWitness(from_addr):
        from_value = Get(ctx, from_addr)
        if from_value < amount:
            print("insufficient funds")
            return False

        if from_value == amount:
            Delete(ctx, from_addr)
        else:
            from_total = from_value - amount
            Put(ctx, from_addr, from_total)

        to_value = Get(ctx, to_addr)
        to_total = to_value + amount
        Put(ctx, to_addr, to_total)
        OnTransfer(from_addr, to_addr, amount)

        return True
    else:
        print("from address is not the tx sender")

    return False
