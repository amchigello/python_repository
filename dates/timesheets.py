import datetime
import calendar
import pandas as pd

CURRENT_DATE = datetime.datetime.today()
CURRENT_YEAR = CURRENT_DATE.year
CURRENT_MONTH = CURRENT_DATE.month

LEAVES = 2
HOLIDAYS = 1


def get_number_of_weekend(days):
    weekend_count = 0
    for day in days:
        if(day.isoweekday() in [6, 7]):
            weekend_count = weekend_count + 1
    return weekend_count


def calculate_days(year, month):
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
    weekend_count = get_number_of_weekend(days)
    working_days = num_days - weekend_count - LEAVES - HOLIDAYS
    return {"YEAR": year,
            "MONTH": calendar.month_name[month],
            "TOTAL_DAYS": num_days,
            "WEEKENDS": weekend_count,
            "LEAVES": LEAVES,
            "PUBLIC_HOLIDAYS": HOLIDAYS,
            "NO_OF_WORKING_DAYS": working_days
            }


def main(year=CURRENT_YEAR, month=CURRENT_MONTH):
    timesheets = calculate_days(year=year, month=month)
    df = pd.DataFrame(data=timesheets, index=[0])
    df.to_csv('timesheets.csv')
    return timesheets


if __name__ == "__main__":
    main(2020,2)

