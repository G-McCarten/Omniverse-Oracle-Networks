# Read from a contract that we already deployed.

from brownie import SimpleStorage, accounts, config


def read_contract():
    # print(SimpleStorage[0])
    # [-1] returns the most recent contract made.
    simple_storage = SimpleStorage[-1]

    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()
