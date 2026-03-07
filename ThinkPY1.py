minutes = int(input("Enter the minute value: "))
sec = int(input("Enter the seconds value: "))
kilo = float(input("Enter the kilometers value: "))
print('Sport caculator')
time = (minutes * 60) + sec
miles= kilo * 0.621371
pace = time / miles
avgspeed = miles / (time / 3600)
print('Your time is: ' + str(time) + ' seconds')
print('Your average speed is: ' + str(avgspeed) + ' miles per hour')
print('Your pace is: ' + str(pace) + ' seconds per miles')
print('Your pace is: ' + str(pace / 60) + ' minutes per miles')