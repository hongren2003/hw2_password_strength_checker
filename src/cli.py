"""CLI compatible with password_checker.py"""

import sys
import password_checker


def main() -> None:
    print("Simple password strength checker")
    print('* If you want to exit, please input "q", "quit", "exit" or "Ctrl-c"')
    while True:
        pwd = input("Password: ")
        if pwd.lower() in ("q", "quit", "exit"):
            print("Bye")
            sys.exit(0)
        ok, msgs = password_checker.check_password(pwd, [])
        if ok:
            print("Password meets strength requirements.")
            sys.exit(0)
        else:
            print("Failed:")
            for m in msgs:
                print(" - ", m)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye")
        sys.exit(130)  # exit with code 130 (keyboard interruption)
