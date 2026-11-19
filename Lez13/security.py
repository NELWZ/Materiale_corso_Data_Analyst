# security.py
import hashlib
import hmac
import os
from typing import Optional


def hash_password(password: str, salt: Optional[bytes] = None) -> str:

    if salt is None:
        salt = os.urandom(16)

    pwd_bytes = password.encode("utf-8")
    hashed = hashlib.pbkdf2_hmac("sha256", pwd_bytes, salt, 100_000)
    return f"{salt.hex()}${hashed.hex()}"


def verify_password(password: str, stored: str) -> bool:
    if stored is None or "$" not in stored:
        return False

    salt_hex, expected_hash = stored.split("$")
    salt = bytes.fromhex(salt_hex)

    pwd_bytes = password.encode("utf-8")
    hashed = hashlib.pbkdf2_hmac("sha256", pwd_bytes, salt, 100_000)
    return hmac.compare_digest(hashed.hex(), expected_hash)