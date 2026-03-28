import time
import hashlib


def jquery_now() -> int:
    return int(time.time() * 1000)


def hex_sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest().upper()
