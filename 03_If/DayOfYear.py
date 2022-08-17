def leapYear(y):
    if (y%4 == 0) and (y%100 != 0 or y%400 == 0):
        return True
    return False

def day_of_year(d, m, y):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapYear(y - 543):
        days[2] += 1
    return sum(days[:m]) + d

day = int(input())
month = int(input())
year = int(input())

print(day_of_year(day, month, year))