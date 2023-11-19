
def check_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_year_leap = check_year(year)
    if is_year_leap and month == 2:
        return (month_days[month - 1] + 1)
    else:
        return month_days[month - 1]


year = int(input("enter a year: "))
month = int(input("enter a month: "))
days = days_in_month(year, month)

print(days)