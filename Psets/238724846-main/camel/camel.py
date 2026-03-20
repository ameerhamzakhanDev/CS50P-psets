
def main():
    camels = input("camelCase: ").strip()
    print(convert(camels))

def convert(camels):
    result = ""

    for camel in camels:
        if camel.isupper():
            result += f"_{camel.lower()}"
        elif camel == " ":
            result += "_"
        else:
            result += camel

    if camels[0].isupper():
        result = result[1:]
    return result

if __name__ == "__main__":
    main()
