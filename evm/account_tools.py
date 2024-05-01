from web3 import Web3
from eth_account.messages import encode_defunct
from logger.logger import logger


def get_web3_simple_entity():
    return Web3()


def sign_string_message(private_key_hex: str, message: str) -> str:
    web3 = get_web3_simple_entity()
    account = web3.eth.account.from_key(private_key_hex)
    message_encoded = encode_defunct(text=message)
    logger.info(f"message_encoded: {message_encoded}")
    signature = account.sign_message(message_encoded)
    logger.info(f"signature: {signature.signature.hex}")
    return signature.signature.hex()


def get_wallet_address(private_key_hex: str) -> str:
    web3 = get_web3_simple_entity()
    account = web3.eth.account.from_key(private_key_hex)
    return account.address
