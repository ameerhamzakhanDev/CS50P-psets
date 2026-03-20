from datetime import datetime, date
import inflect
from sys import exit

class DateToMin:

    p = inflect.engine()

    def __int__(self, date):
        self.date = date

    @classmethod
    def verify_date(cls, date: str, dateformat =  "%Y-%m-%d"):
        try:
            datetime.strptime(date, dateformat)
        except ValueError:
            exit(f"{date} is not a valid date.")

    @classmethod
    def convert(cls, bdate):

        tday = date.today()
        bdate = datetime.strptime(bdate, "%Y-%m-%d").date()
        time = tday - bdate
        tmins = time.days * 24 * 60
        return (f"{cls.p.number_to_words(int(tmins), andword='')} minutes").capitalize()



def main():

    date = input("Date of Birth: ")

    DateToMin.verify_date(date)
    print(DateToMin.convert(date))






if __name__ == "__main__":
    main()
