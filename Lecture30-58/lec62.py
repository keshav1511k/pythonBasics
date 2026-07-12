# Date and time

import datetime

date = datetime.date(2025, 1, 25)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S  %m-%d-%Y")

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)  # (year, month, date, hour, minute, second)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("The time has passed")
else:
    print("The time has not passed yet")