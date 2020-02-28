import datetime
import calendar
import pandas as pd

CURRENT_DATE = datetime.datetime.today()
CURRENT_YEAR = CURRENT_DATE.year
CURRENT_MONTH = CURRENT_DATE.month

HOLIDAYS_DICT = {2020: ['2020-01-01', '2020-01-15', '2020-02-21',
                        '2020-03-10', '2020-03-25', '2020-04-10',
                        '2020-05-01', '2020-05-25', '2020-10-02',
                        '2020-10-26', '2020-11-16', '2020-12-25']}

LEAVES = 0


def calculate_days(year, month):
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
    weekend_count = len([day for day in days if day.isoweekday() in [6, 7]])
    holiday_list = [datetime.datetime.strptime(
        day, '%Y-%m-%d').date() for day in HOLIDAYS_DICT[2020]]
    holidays = len(set(holiday_list) & set(days))
    working_days = num_days - weekend_count - LEAVES - holidays
    return {"YEAR": year,
            "MONTH": calendar.month_name[month],
            "TOTAL_DAYS": num_days,
            "WEEKENDS": weekend_count,
            "LEAVES": LEAVES,
            "PUBLIC_HOLIDAYS": holidays,
            "NO_OF_WORKING_DAYS": working_days
            }


def main(year=CURRENT_YEAR, month=CURRENT_MONTH):
    timesheets = calculate_days(year=year, month=month)
    df = pd.DataFrame(data=timesheets, index=[0])
    df.to_csv('timesheets.csv')
    return timesheets


if __name__ == "__main__":
    # main(2020,2)
    main()

