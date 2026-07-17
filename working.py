import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)', s)
    if match:
        start_h, start_m, start_period, end_h, end_m, end_period = match.groups()
        start_m = start_m or '00'   # if no minutes, default to 00
        end_m = end_m or '00'
        start_h = int(start_h)
        end_h = int(end_h)
        if int(start_m) > 59 or int(end_m) > 59:
            raise ValueError
        if start_period == 'PM' and start_h != 12:
            start_h += 12
        if start_period == 'AM' and start_h == 12:
            start_h = 0
        if end_period == 'PM' and end_h != 12:
            end_h += 12
        if end_period == 'AM' and end_h == 12:
            end_h = 0
        return f'{start_h:02d}:{start_m} to {end_h:02d}:{end_m}'
    else:
        raise ValueError

if __name__ == "__main__":
    main()
