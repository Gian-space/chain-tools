from web3 import Web3


class Transaction:
    def __init__(self, rpc):
        self.web3 = Web3(Web3.HTTPProvider(rpc))

    def get_gas_price(self):
        return self.web3.eth.gas_price

    def estimate_gas(self):
        return self.web3.eth.estimate_gas()

