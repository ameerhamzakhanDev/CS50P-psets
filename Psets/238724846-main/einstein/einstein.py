def main():
    s = int(input("m: "))
    print(convert(s))

def convert(mass: int):
    E = mass * ((300000000) ** 2)
    return E



if __name__ == "__main__":
    main()


