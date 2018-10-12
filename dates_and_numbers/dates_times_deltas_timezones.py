# References https://www.youtube.com/watch?v=eirjjyP2qcQ&t=0s
# https://docs.python.org/3/library/datetime.html#timezone-objects
# Python has dates, times, timezones, datetimes, & timedeltas
# Main module is datetime
# Naive dates don't have enough info to determine timezone, DST
# Aware dates have enough info, but are more complex to use
# Date gives y, m, d time gives h, m, s, micro-s
# Datetime gives both of above
# Always recommended to work with UTC when using timezones

# Should use the dateutil package, pytz used just to follow tutorial

import datetime
import pytz  # Downloaded package

# Needs as integers without a leading zero
d = datetime.date(2016, 7, 24)
print(d)
today = datetime.date.today()
print(today)
print(today.year)
print(today.weekday())  # Monday is 0, sunday is 6
print(today.isoweekday())  # Monday is 1, sunday is 7
print("Time deltas below\n")
time_delta = datetime.timedelta(days=7)
print(today + time_delta)  # Can add offset to a date
print(today - time_delta)
birthday = datetime.date(2019, 6, 19)
until_birthday = birthday - today
print(until_birthday)
print(until_birthday.days)
print(until_birthday.total_seconds())
print("time attribute included below\n")
# By default, is naive - no timezone info
t = datetime.time(9, 30, 45, 100000)  # H, m, s, microseconds
print(t)
# Have pretty much anything needed
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.time())  # Can call on specific attributes
print(dt.date())
print(dt.year)
time_delta = datetime.timedelta(hours=7)
print(dt + time_delta)
print("Alternative constructors below\n")
# .today returns current local datetime with timezone of None
dt_today = datetime.datetime.today()  # Returns current local date time
dt_now = datetime.datetime.now()  # Allows timezone to pass in
# utc has timezone set to None
dt_utc_now = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utc_now)
print("UTC below via pytz\n")
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)  # Has UTC offset
dt_now = datetime.datetime.now(tz=pytz.UTC)  # Same result, less typing
dt_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_now)
print(dt_utc_now)
print("\nTimezone conversion below\n")
dt_utc_now = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt_utc_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_utc_now)
print(dt_mtn)
# Can see all available timezones via below
# for tz in pytz.all_timezones:
#     print(tz)
print("\nNaive datetime conversion below\n")
dt_mtn = datetime.datetime.now()
print(dt_mtn)  # Without timezone data
# Won't work, dt_mtn is a naive timezone
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)  # Localizes a naive datetime
print(dt_mtn)  # Now timezone aware
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
print("\nDisplay methods below\n")
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# Format codes at Python documentation library
print(dt_mtn.strftime("%B %d, %Y"))
dt_str = "October 12, 2018"
# Same format codes as above for taking in a string
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)
