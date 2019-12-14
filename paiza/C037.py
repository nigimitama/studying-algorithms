date, time = input().split()
hour, minute = list(map(int, time.split(":")))
month, day = list(map(int, date.split("/")))
day_ex, hour = divmod(hour, 24)
day += day_ex

print(str(month).zfill(2)+"/"+str(day).zfill(2), str(hour).zfill(2)+":"+str(minute).zfill(2))
