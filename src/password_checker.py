"""
A simple password checker
"""

from typing import List, Callable, Tuple

SPECIAL_CHARS = set("!@#$%^&*")


def rule_length(password: str) -> Tuple[bool, str]:
    """Check if the length of password meets the minimum requirement.

    Args:
        password (str)

    Returns:
        Tuple[bool, str]: (Passed or not, error)
    """
    return len(password) >= 8, "Password must be at least 8 characters long."


def rule_uppercase(password: str) -> Tuple[bool, str]:
    """Check if the password contains at least one uppercase letter.

    Args:
        password (str)

    Returns:
        Tuple[bool, str]: (Passed or not, error)
    """
    return (
        any("A" <= c <= "Z" for c in password),
        "Password must contain an uppercase letter.",
    )


def rule_lowercase(password: str) -> Tuple[bool, str]:
    """Check if the password contains at least one lowercase letter.

    Args:
        password (str)

    Returns:
        Tuple[bool, str]: (Passed or not, error)
    """
    return (
        any("a" <= c <= "z" for c in password),
        "Password must contain a lowercase letter.",
    )


def rule_digit(password: str) -> Tuple[bool, str]:
    """Check if the password contains at least one digit.

    Args:
        password (str)

    Returns:
        Tuple[bool, str]: (Passed or not, error)
    """
    return any("0" <= c <= "9" for c in password), "Password must contain a digit."


def rule_special(password: str) -> Tuple[bool, str]:
    """Check if the password contains at least one special symbol.

    Args:
        password (str)

    Returns:
        Tuple[bool, str]: (Passed or not, error)
    """
    return (
        any(c in SPECIAL_CHARS for c in password),
        "Password must contain a special character (!@#$%^&*).",
    )


def rule_no_triple_repeat(password: str) -> Tuple[bool, str]:
    """Check if the password have no triple (or more) repeat.

    Args:
        password (str)

    Returns:
        Tuple[bool, str]: (Passed or not, error)
        Note: error only outputs the starting position of the first repeat.
    """
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return (
                False,
                f"Your password has consecutive repeats starting from offset {i}",
            )
    return True, ""


def check_password(
    password: str, custom_rules: List[Callable[[str], Tuple[bool, str]]]
) -> Tuple[bool, List]:
    """Check if the password meets all the given policies and give error message
    when it is possible.

    Args:
        password (str):
        custom_rules (List[Callable[[str], Tuple[bool, str]]]): List of policy functions
        defined above

    Returns:
        Tuple[bool, List]: (Passed or not, list of failures and their msg)
    """
    rule_set = custom_rules or [
        rule_length,
        rule_uppercase,
        rule_lowercase,
        rule_digit,
        rule_special,
        rule_no_triple_repeat,
    ]

    failures = [msg for ok, msg in (r(password) for r in rule_set) if not ok]
    return not failures, failures
