import argparse
import base64
import os
import sys
from getpass import getpass

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


VERSION_PREFIX = b"v1"
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_LENGTH = 32


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=KEY_LENGTH, n=2 ** 14, r=8, p=1)
    return kdf.derive(password.encode("utf-8"))


def encrypt(text: str, password: str) -> str:
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)
    key = derive_key(password, salt)
    ciphertext = AESGCM(key).encrypt(nonce, text.encode("utf-8"), None)
    payload = VERSION_PREFIX + salt + nonce + ciphertext
    return base64.urlsafe_b64encode(payload).decode("ascii")


def decrypt(data_b64: str, password: str) -> str:
    data = base64.urlsafe_b64decode(data_b64.encode("ascii"))
    if data[: len(VERSION_PREFIX)] != VERSION_PREFIX:
        raise ValueError("unsupported version")

    salt_start = len(VERSION_PREFIX)
    salt_end = salt_start + SALT_SIZE
    nonce_end = salt_end + NONCE_SIZE

    salt = data[salt_start:salt_end]
    nonce = data[salt_end:nonce_end]
    ciphertext = data[nonce_end:]

    key = derive_key(password, salt)
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Eenvoudige AES-256-GCM encryptie/ decryptie"
    )
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Kies encrypt of decrypt")
    parser.add_argument("--text", help="Tekst om te versleutelen")
    parser.add_argument("--data", help="Base64 data om te ontsleutelen")
    parser.add_argument(
        "--password", help="Wachtwoord (laat leeg voor interactieve invoer)"
    )
    args = parser.parse_args()

    try:
        password = args.password or getpass("Voer wachtwoord in: ")

        if args.mode == "encrypt":
            text = args.text or input("Tekst om te versleutelen: ")
            print(encrypt(text, password))
        else:
            data_b64 = args.data or input("Base64 data om te ontsleutelen: ")
            print(decrypt(data_b64, password))
        return 0
    except Exception as exc:  
        print(f"Fout: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())