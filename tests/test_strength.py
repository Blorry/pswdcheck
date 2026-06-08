import string

from app.strength import character_pool_size, classify, estimate_bits, generate


def test_pool_size_lower_only():
    assert character_pool_size("abc") == 26


def test_pool_size_all_classes():
    expected = 26 + 26 + 10 + len(string.punctuation)
    assert character_pool_size("aB3!") == expected


def test_empty_password_zero_bits():
    assert estimate_bits("") == 0.0


def test_longer_password_more_bits():
    assert estimate_bits("aaaaaaaa") > estimate_bits("aaa")


def test_classify_boundaries():
    assert classify(10) == "weak"
    assert classify(40) == "medium"
    assert classify(100) == "strong"
    assert classify(200) == "very strong"


def test_generate_length():
    assert len(generate(20)) == 20


def test_generate_is_random():
    assert generate(16) != generate(16)
