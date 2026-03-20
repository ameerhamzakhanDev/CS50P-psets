
while True:
    try:
        x, y = input("Fraction: ").strip().split("/")
        x, y = int(x), int(y)
    except :
        print("Please enter valid positive integers and a \"/\" in between")
        continue
    if x > y or y == 0 or x < 0 or y < 0:
        continue

    fraction = int(round((x / y) * 100, 0))

    if fraction <= 1:
        print("E")
        break
    elif fraction >= 99:
        print("F")
        break
    else:
        print(f"{fraction}%")
        break

