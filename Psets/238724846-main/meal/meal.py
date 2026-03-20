def main():
    time = input("What's the time? ").strip()
    meal =  convert(time)
    if meal >= 7 and meal <= 8:
        print("breakfast time")
    if meal >= 12 and meal <= 13:
        print("lunch time")
    if meal >= 18 and meal <= 19:
        print("dinner time")



def convert(time: str):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)/60
    return hours + minutes



if __name__ == "__main__":
    main()
