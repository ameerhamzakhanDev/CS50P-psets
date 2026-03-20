import sys
import csv


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments ")
    elif not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")
    try:
        with open(f"{sys.argv[1]}", "r") as f:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(pizza_menu())


def pizza_menu():

    with open(f"{sys.argv[1]}", "r") as f, open(sys.argv[2], "w") as n:

        reader = csv.DictReader(f)
        writer = csv.DictWriter(n, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            writer.writerow({
                "first" : first,
                "last" : last,
                "house" : house
            })




if __name__ == "__main__":
    main()
