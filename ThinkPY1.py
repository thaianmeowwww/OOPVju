minutes = int(input("Enter the minute value: "))
sec = int(input("Enter the seconds value: "))
kilo = float(input("Enter the kilometers value: "))
print('Sport caculator')
time = (minutes * 60) + sec
miles= kilo * 0.621371
pace = time / miles
avgspeed = miles / (time / 3600)
print('Your time is: ' + str(round(time, 2)) + ' seconds')
print('Your average speed is: ' + str(round(avgspeed, 2)) + ' miles per hour')
print('Your pace is: ' + str(round(pace, 2)) + ' seconds per miles')
print('Your pace is: ' + str(round(pace / 60, 2)) + ' minutes per miles')