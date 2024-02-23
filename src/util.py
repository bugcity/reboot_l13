import time
import hashlib


class DictToClass:
    def __init__(self, dictionary: dict):
        for key, value in dictionary.items():
            setattr(self, key, value)


def jquery_now() -> int:
    return int(time.time() * 1000)


def hex_sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest().upper()


def password_algorithms_cookie(s: str) -> str:
    return hex_sha256(s)
