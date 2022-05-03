from brownie import accounts, config, Contract, EasyToken
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20_address = config["arbitrary"]["erc_address"]
    recipients = config["arbitrary"]["recipient"]
    amount = 10000000000000000
    erc20 = Contract.from_abi("EasyToken", erc20_address, EasyToken.abi)
    tx = erc20.transfer(recipients, amount, {"from": account})
    tx.wait(1)