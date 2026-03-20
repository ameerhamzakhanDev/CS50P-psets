import ttkbootstrap as ttk
import csv
from datetime import datetime, date
import random


# File paths
csv_file = "checkin.csv"
quotes_file = "quotes.txt"


def main():
    csv_setup()
    window_setup()


def csv_setup():
    try:
        # Try to open the file
        with open(csv_file, 'r') as file:
            pass
    except FileNotFoundError:
        # setting up the file
        with open(csv_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["day", "date"])
            writer.writeheader()
            today = str(datetime.today().date())
            writer.writerow({"day": 1, "date" : today})


def window_setup():
    # window
    window = ttk.Window(themename = "journal")
    window.title("Daily Checkup")
    window.geometry("600x300")
    window.iconbitmap("CS50P.ico")

    label = ttk.Label(master = window, text = "Let's do Today's Checkup!", font = ("Verdana bold", 20))

    button = ttk.Button(master = window, text = "Check", command = check_in)
    global output_str
    output_str = ttk.StringVar()
    output_label = ttk.Label(master = window, text = "Congratulations!", font = ("Verdana", 14), textvariable = output_str )

    global streak_str
    streak_str = ttk.StringVar()
    streak_label = ttk.Label(master = window, text = "<streak>", font = ("Verdana", 14), textvariable = streak_str )

    quote_frame = ttk.Frame(master = window, width=200, height=200)
    global quote_str
    quote_str = ttk.StringVar()
    quote_label = ttk.Label(master = quote_frame, text = "<quote>", font = ("Times New Roman", 12), textvariable = quote_str, wraplength=400, justify = "center")

    # Packing


    label.pack(pady = 20)
    button.pack()
    output_label.pack(pady= 15)
    streak_label.pack()
    quote_label.pack(pady = 5)
    quote_frame.pack()

    window.mainloop()



def quote_generator():
    with open(quotes_file, "r") as file:
        quote = random.choice(file.readlines())
        return quote

def streak_message(streak):
    # If today's date is the same
    if (streak == 0):
        return "Checked in for the day!"

# Check if today's date is later than the last checked-in date
    elif streak == 1:
        globals()["day"] += 1
        return "Checked in!"

    elif (streak > 1):
        globals()["day"] = 1
        return "You took to long!"

# hopefully will never execute with malicious intent
    else:
        return "Something is wrong with checkin.csv"


# This was completely unneccsary but I had to make it for the test file
def calculate_streak(today, last_date):
    return (today - last_date).days



def check_in():
    # extracting day(streak) and date
    with open(csv_file, "r", newline="") as file:
        global day
        day, last_date = (list(file)[-1].strip().split(","))
        day = int(day)
        last_date = date.fromisoformat(last_date)

    # BACKBONE of program:
    today = datetime.today().date()
    streak = calculate_streak(today=today, last_date=last_date)
    message = streak_message(streak=streak)


    output_str.set(message)


    with open(csv_file, "a", newline="") as file1:
        writer = csv.DictWriter(file1, fieldnames=["day", "date"])
        if streak != 0:
            writer.writerow({"day": day, "date" : today})

    streak_str.set(f"Streak: {day}")
    quote_str.set(f'''Quote of the day:
{quote_generator()}''')




if __name__ == "__main__":
    main()


