def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not len(s) <= 6 and len(s) >= 2:
        return False

    # No periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False

    #All vanity plates must start with at least two letters
    elif s[0:2].isdigit():
        return False

    # # Numbers cannot be used in the middle of a plate; they must come at the end.
    elif not ((s[2:].isdigit() or s[3:].isdigit()) or (s[4:].isdigit() or s[5:].isalpha())):
        return False

    # The first number used cannot be a ‘0’
    for num in s:
        if num.isdigit() and num == "0":
            return False
        if num.isdigit():
            return True
        else:
            continue

    else:
        return True


main()
