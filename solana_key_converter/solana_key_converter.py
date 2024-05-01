import os
import json
import base58


def convert_to_json(filename):
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        raise EnvironmentError("PRIVATE_KEY not defined in environment. Please define it.")

    private_key_array = list(base58.b58decode(private_key))
    with open(filename, 'w') as file:
        json.dump(private_key_array, file)
    print("Private key has been converted to JSON file.")


def convert_to_private_key(filepath):
    with open(filepath, 'r') as file:
        private_key_array = json.load(file)
    private_key = base58.b58encode(bytes(private_key_array)).decode('utf-8')
    print("Private key is: ", private_key)


if __name__ == "__main__":
    pass
