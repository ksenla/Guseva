date = input("Напишите дату в виде: дд.мм.гггг:")
day, month, year = map(int, date.split('.'))
if day * month == int(str(year)[-2:]):
    print ("дата является магической")
else:
    print ("дата не является магической")