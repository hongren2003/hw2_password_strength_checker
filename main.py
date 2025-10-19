from sys import exit
from src.password_strength_checker.password_strength_checker import check_password_strength


def main():
    while True:
        user_input = input("Provide a password: ")
        if user_input is ":q":
            exit()
        result = check_password_strength(user_input)
        if result[0] is True:
            print("Password meets strength requirements.")
            exit()
        elif result[1] is False:
            print("Password does NOT meet strength requirements")
            print("")

if __name__ == "__main__":
    main()
