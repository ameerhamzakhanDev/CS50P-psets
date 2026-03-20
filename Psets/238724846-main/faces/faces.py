def main():
    s = input("Do you like cats? ")
    print(convert(s))

def convert(string: str):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")

    return string


if __name__ == "__main__":
    main()


