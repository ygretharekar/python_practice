import calendar

if __name__ == '__main__':
    date = input().split()
    days = list(calendar.day_name)
    print(days[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))].upper())
