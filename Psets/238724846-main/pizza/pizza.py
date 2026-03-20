import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments ")
    elif  not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    print(pizza_menu())



def pizza_menu():
    try:
        with open(f"{sys.argv[1]}", "r") as f:
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(f"{sys.argv[1]}", "r") as f:

        lines = csv.DictReader(f)

        menu = tabulate(lines, headers="keys", tablefmt="grid")
        return menu


if __name__ == "__main__":
    main()
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
