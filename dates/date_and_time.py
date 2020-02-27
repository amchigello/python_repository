import datetime
import pytz

# Set Date
d = datetime.date(2020, 2, 25)
print(d)

# Setting todays date
today = datetime.date.today()
print(today)
print("Year is {}".format(today.year))
print("Month is {}".format(today.month))
print("Day is {}".format(today.day))
print("Weekday is {}".format(today.weekday()))  # Monday 0, Sunday 6
print("ISO WeekDay is {}".format(today.isoweekday()))  # Monday 1, Sunday 7

# Time deltas: Difference between two dates
tdelta = datetime.timedelta(days=7)
print("Today + {} days is {}".format(tdelta.days, today+tdelta))
print("Today - {} days is {}".format(tdelta.days, today-tdelta))

# Timedelta of two days
birthday = datetime.date(1989, 5, 1)
dob_today_delta = today-birthday
print("Days from DOB {} is {}".format(birthday, dob_today_delta.days))
print("Seconds from DOB {} is {}".format(
    birthday, dob_today_delta.total_seconds()))


############################################################################################
# Datetime

t = datetime.time(14, 12, 34, 452134)
print("Hour is {}".format(t.hour))
print("Microseconds is {}".format(t.microsecond))
print("Seconds is {}".format(t.second))

today = datetime.datetime.now()
print(today.date())
print(today.time())
print("Year is {}".format(today.year))
print("Month is {}".format(today.month))
print("Day is {}".format(today.day))
print("Hour is {}".format(today.hour))
print("Minute is {}".format(today.minute))
print("Seconds is {}".format(today.second))
print("Microseconds is {}".format(today.microsecond))


#####################################
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print("dt_today : {}".format(dt_today))
print("dt_now : {}".format(dt_now))
print("dt_utcnow : {}".format(dt_utcnow))

#####################################


dt = datetime.datetime(2020, 1, 26, 11, 22, 33, tzinfo=pytz.utc)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utc = dt_now.astimezone(pytz.timezone("Asia/Kolkata"))
print(dt_utc)

for tz in pytz.all_timezones:
    print(tz)


#Date to String
print("Formatted date {}".format(dt_utc.strftime("%B %d, %Y")))


#String to Date
dt_str="25-Jan-2020"
dt_str_converted =datetime.datetime.strptime(dt_str,'%d-%b-%Y')
print(dt_str_converted)
