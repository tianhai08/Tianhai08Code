import calendar

def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

def main():
    year = 2023
    month = 6
    print_calendar(year, month)

if __name__ == "__main__":
    main()
