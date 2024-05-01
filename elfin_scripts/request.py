import json
from logger.logger import logger
import requests


def get_nonce():
    url = "https://api.elfin.games/testnet/client/passport/nonce"
    # TODO Fake
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
        "authorization": "Bearer",
        "content-type": "application/json"
    }
    data = {
        "walletAddress": "0x3c890d1e14b756d3b77b0d63d31900a7c340b251"
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()


def auth(invite_code: str = "",walletAddress: str = "",signature: str = "",network: int = 1,publicKey: str = ""):
    logger.info(f"invite_code: {invite_code}, walletAddress: {walletAddress}, signature: {signature}, network: {network}, publicKey: {publicKey}")

    url = 'https://api.elfin.games/testnet/client/passport/auth'
    # TODO Fake
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'authorization': 'Bearer',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://elfin.games',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://elfin.games/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    data = {
        "walletAddress": walletAddress,
        "signature": signature,
        "network": network,
        "publicKey": "",
        "inviteCode": invite_code
    }

    logger.info(f"auth data: {data}")
    response = requests.post(url, data=json.dumps(data), headers=headers)
    logger.info(f"auth response: {response.json()}")
    return response.json()


if __name__ == '__main__':
    nonce = get_nonce().get("nonce")
