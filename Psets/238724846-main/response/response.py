import validators


def main():
    email = input("Enter a email: ")
    print(is_vaild(email), end="")


def is_vaild(email):
    valid = validators.email(email)
    if valid:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
