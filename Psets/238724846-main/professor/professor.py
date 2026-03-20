import random


def main():
    level = get_level()

    mistake = 0
    score = 0

    q = 0

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        sol = x + y

        while True:
            try:
                ans = int(input(f"{x} + {y} = "))

            except ValueError:
                print("EEE")
                mistake += 1
                if mistake == 3:
                    print(f"{x} + {y} = {sol}")
                    mistake = 0
                    q += 1
                    break
                continue

            if ans != sol:
                print("EEE")
                mistake += 1
            else:
                score += 1
                break

            if mistake == 3:
                print(f"{x} + {y} = {sol}")

                mistake = 0
                break

    print(f"Score: {score}")



def get_level():

    while True:
        try:
            l = int(input("Level: "))

        except ValueError:
            print("Give a valid number!")
            continue

        if not (int(l) == 1 or int(l) == 2 or int(l) == 3):
            continue
        else:
            return l


def generate_integer(level):


    if level == 1:
        return random.randint(0, 9)

    if level == 2:
        return random.randint(10, 99)

    if level == 3:
        return random.randint(100, 999)




if __name__ == "__main__":
    main()
