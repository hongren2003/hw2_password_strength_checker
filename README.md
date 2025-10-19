# Password Strength Checker

Public repository link: https://github.com/hongren2003/hw2_password_strength_checker

Hong-Ren (Raymond) Huang (M610114003)

Graduate Institute of Biomedical Informatics, Taipei Medical University

3100E186: Fundamentals of programming design

October 19, 2025

## Description

This is a comprehensive password validation system written in Python.

Default password strength requirements:

1. Length of at least 8 characters
1. Includes at least one uppercase letter
1. Includes at least one lowercase letter
1. Includes at least one digit
1. Includes at least one special character from `!@#$%^&*`
1. No more than 2 identical characters in a row (i.e., no 3+ consecutive repeats)

### Interactive input & validation

1. Continuously prompt the user to enter a password and check it against each strength requirement.

1. If any requirement is not met, display the specific reason and prompt the user to try again.

1. If all requirements pass, display “Password meets strength requirements.” and terminate the program.

### Quit/abort option

If you don't wish to continue, they may enter "q", "quit", "exit" or directly "Ctrl-c" to abort immediately.

## How to run?

You can simply run the `cli.py` under `src/` with `python` to access the CLI tool.

```bash
python src/cli.py
```

If your system has Python 2 and 3 installed simultaneously, you may need use `python3` explicitly instead of `python`.

## Tests

This project uses `pytest` as the testing framework. The rules are specified in the directory `tests`.

If you use `uv`, you can directly run the command

```bash
uv run pytest
```

You may want to refer to https://docs.astral.sh/uv/ to find the appropriate way to install `uv` on your operating system.

If you don't want to use `uv`, you can use native Python from your system as the follows:

```bash
python3 -m venv .venv
source .venv/bin/activate.    # -nix or MacOS
source venv\Scripts\activate  # Windows
pip install -e .
pip install pytest
python -m pytest
```
