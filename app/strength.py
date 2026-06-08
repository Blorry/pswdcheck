import math
import secrets
import string

LOWER = set(string.ascii_lowercase)
UPPER = set(string.ascii_uppercase)
DIGITS = set(string.digits)
SYMBOLS = set(string.punctuation)

POOL_SIZES = (
    (LOWER, 26),
    (UPPER, 26),
    (DIGITS, 10),
    (SYMBOLS, len(string.punctuation)),
)


def character_pool_size(password):
    chars = set(password)
    size = 0
    for group, count in POOL_SIZES:
        if chars & group:
            size += count
    extra = chars - LOWER - UPPER - DIGITS - SYMBOLS
    size += len(extra)
    return size


def estimate_bits(password):
    if not password:
        return 0.0
    pool = character_pool_size(password)
    if pool == 0:
        return 0.0
    return round(len(password) * math.log2(pool), 2)


def classify(bits):
    if bits < 28:
        return "weak"
    if bits < 60:
        return "medium"
    if bits < 128:
        return "strong"
    return "very strong"


def check(password):
    bits = estimate_bits(password)
    return {
        "length": len(password),
        "pool_size": character_pool_size(password),
        "entropy_bits": bits,
        "strength": classify(bits),
    }


def generate(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))
