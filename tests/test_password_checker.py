"""Tester for password_checker.py"""

import pytest
from src.password_checker import (
    rule_length,
    rule_uppercase,
    rule_lowercase,
    rule_digit,
    rule_special,
    rule_no_triple_repeat,
    check_password,
)

# Single test


def test_rule_length():
    assert rule_length("12345678")[0] is True
    assert rule_length("short")[0] is False


def test_rule_uppercase():
    assert rule_uppercase("abcD")[0] is True
    ok, msg = rule_uppercase("abcd")
    assert not ok
    assert "uppercase" in msg.lower()


def test_rule_lowercase():
    assert rule_lowercase("aBC")[0] is True
    ok, msg = rule_lowercase("ABC")
    assert not ok
    assert "lowercase" in msg.lower()


def test_rule_digit():
    assert rule_digit("pass123")[0] is True
    ok, msg = rule_digit("no_digits")
    assert not ok
    assert "digit" in msg.lower()


def test_rule_special():
    assert rule_special("abc@123")[0] is True
    ok, msg = rule_special("abc123")
    assert not ok
    assert "special" in msg.lower()


def test_rule_no_triple_repeat_pass():
    assert rule_no_triple_repeat("aabbcc")[0] is True


def test_rule_no_triple_repeat_fail():
    ok, msg = rule_no_triple_repeat("aaabbb")
    assert not ok
    assert "offset" in msg
    assert "0" in msg


# Comprehensive tests


def test_check_password_all_pass():
    pwd = "Abc!2345"
    ok, msgs = check_password(pwd, [])
    assert ok
    assert msgs == []


def test_check_password_multiple_failures():
    pwd = "abc"
    ok, msgs = check_password(pwd, [])
    assert not ok
    assert any("uppercase" in m.lower() for m in msgs)
    assert any("digit" in m.lower() for m in msgs)
    assert any("special" in m.lower() for m in msgs)


def test_check_password_triple_repeat():
    pwd = "AAAaaa!!!"
    ok, msgs = check_password(pwd, [])
    assert not ok
    assert any("consecutive" in m.lower() for m in msgs)


def test_check_password_custom_rule():
    def dummy_rule(pwd: str):
        return False, "Custom rule failed."

    ok, msgs = check_password("ValidPass1!", [dummy_rule])
    assert not ok
    assert msgs == ["Custom rule failed."]


def test_check_password_empty_string():
    ok, msgs = check_password("", [])
    assert not ok
    assert any("at least 8 characters" in m.lower() for m in msgs)


def test_check_password_edge_case_long_input():
    long_pwd = "Aa1!" * 1000  # It should meet all requirements
    ok, msgs = check_password(long_pwd, [])
    assert ok
    assert msgs == []
