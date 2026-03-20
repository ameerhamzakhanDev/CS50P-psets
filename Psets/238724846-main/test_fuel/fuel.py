def main():
    while True:
        try:
            x, y = input("Fraction: ").strip().split("/")
            x, y = int(x), int(y)
            x/y

        except (ValueError, ZeroDivisionError):
            print("Please enter valid positive integers, a \"/\" in between and not divided by 0")
            continue
        if x > y or x < 0 or y < 0:
            continue
        else:
            break
    f = f"{x}/{y}"

    frac = convert(f)
    frac = gauge(frac)
    print(frac)



def convert(f):

    x, y = f.strip().split("/")
    x, y = int(x), int(y)
    x/y

    if x > y or x < 0 or y < 0:
        raise ValueError
    else:
        pass

    fraction = int(round((x / y) * 100, 0))
    return fraction


def gauge(fraction):

    if fraction <= 1:
        return "E"

    elif fraction >= 99:
        return "F"

    else:
        return f"{fraction}%"





if __name__ == "__main__":
    main()
