def main():

    print(remain())

def remain():
    due = 50
    paid = 0
    while due > 0:
        print("Amount Due:", due)
        paid = int(input("Insert coin: "))
        if paid == 25:
            due -= 25
        elif paid == 10:
            due -= 10
        elif paid == 5:
            due -= 5
    if due <= 0:
        return f"Change Owed: {due * -1}"



if __name__ == "__main__":
    main()
