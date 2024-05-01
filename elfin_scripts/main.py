import os
from dotenv import load_dotenv
from logger.logger import logger
from elfin_scripts.request import get_nonce, auth
from evm.account_tools import sign_string_message, get_wallet_address

if __name__ == '__main__':
    logger.info("start-------------------------------------------------")
    load_dotenv('elfin.env')
    private_key = os.getenv("PRIVATE_KEY")
    invite_code = os.getenv("INVITE_CODE")
    wallet_address = get_wallet_address(private_key)

    logger.info(f"wallet_address: {wallet_address} ,invite_code: {invite_code}")

    nonce_msg = get_nonce().get("nonce")
    if nonce_msg:
        signature_result = sign_string_message(private_key, nonce_msg)

        auth_response = auth(invite_code=invite_code, walletAddress=wallet_address,
                             signature=signature_result, network=1, publicKey="")
        Bearer_token = auth_response.get("token")
        logger.info(f"Bearer_token: {Bearer_token}")
    logger.info("end-------------------------------------------------")