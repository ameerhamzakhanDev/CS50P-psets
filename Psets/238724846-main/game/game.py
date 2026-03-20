import random
from sys import exit

while True:
    level = input("Level: ").strip()
    if level.isdigit():
        if not int(level) > 0:
            continue
        else:
            break
    else:
        break


while True:

    if int(level) == 1:
        rand_num = 1
    else:
        rand_num = random.randrange(1, int(level))

    guess = input("Guess: ")
    try:
        guess = int(guess)
    except ValueError:
        continue

    if guess <= 0:
        continue
    elif guess > rand_num:
        print("Too large!")
    elif guess < rand_num:
        print("Too small!")
    else:
        print("Just right!")
        exit()

