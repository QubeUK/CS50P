from validator_collection import checkers

def main():
    email = checkers.is_email(input("What's your email address? "))
    if email:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
