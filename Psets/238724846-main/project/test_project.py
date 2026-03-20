from project import quote_generator, streak_message, calculate_streak, date

def test_quote_generator():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    assert quote_generator() in quotes

def test_streak_message():
    assert streak_message(streak=0) == "Checked in for the day!"
    assert streak_message(streak=-1) == "Something is wrong with checkin.csv"

def test_calculate_streak():
    assert calculate_streak(date(2023, 10, 2), date(2023, 10, 1)) == 1
    assert calculate_streak(date(2023, 10, 1), date(2023, 10, 1)) == 0
    assert calculate_streak(date(2023, 10, 5), date(2023, 10, 1)) == 4
