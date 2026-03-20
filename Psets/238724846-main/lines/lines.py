import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments ")
    elif  not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    print(code_lines())


def code_lines():
    try:
        with open(f"{sys.argv[1]}", "r") as f:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

    num = 0
    with open(f"{sys.argv[1]}", "r") as f:

        lines = f.readlines()

        for line in lines:
            if (line.strip().startswith("#") or line.strip(" ") == "\n" ):
                pass
            else:
                num += 1
        return num


if __name__ == "__main__":
    main()
