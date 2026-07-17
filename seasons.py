from datetime import date
import inflect
import sys


p = inflect.engine()


def main():
    dob = get_date()
    today = date.today()
    days = (today-dob).days
    minutes = days * 24 * 60
    print(p.number_to_words(minutes, andword='').capitalize() + ' minutes')


def minutes_between(dob, today):
    return (today - dob).days * 24 * 60


def get_date():
    while True:
        try:
            dob = date.fromisoformat(input('Date of Birth: '))
            return dob
        except ValueError:
            sys.exit('Invalid Date')


if __name__ == "__main__":
    main()
