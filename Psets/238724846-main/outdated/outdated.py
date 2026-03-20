
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ").strip().title()


    if date[0].isdigit() and ("/" in date): # Check format: MM/DD/YYYY
        date = date.split("/")
        if int(date[0]) > 13 or int(date[1]) > 32:
            continue

        date [0] = f"{int(date[0]):02}"
        date [1] = f"{int(date[1]):02}"

        print(f"{date[2]}-{date[0]}-{date[1]}")
        break


    if date[0].isalpha(): # Check format: MM DD, YYYY
        if not ", " in date:
            continue
        date = date.replace(",", "").split()
        if not ((date[0] in months) and int(date[1]) < 32):
            continue


        date [1] = f"{int(date[1]):02}"

        print(f"{date[2]}-{(int(months.index(date[0])) + 1):02}-{date[1]}")
        break

