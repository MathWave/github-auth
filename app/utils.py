import hashlib

import config


def hash_password(password: str) -> str:
    new_pass = password + config.SECRET_KEY
    hashed = hashlib.md5(new_pass.encode())
    return hashed.hexdigest()
