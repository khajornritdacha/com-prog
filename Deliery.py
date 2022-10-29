def dayInMonth(month: int, year: int) -> int:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2:
        return days[month - 1]
    return days[1] + (year%400 == 0 or (year%4 == 0 and year%100 != 0))

def validate(dtype: str, day: int, month: int, year: int) -> str:
    if year < 2558: return "Invalid year"
    if month < 1 or month > 12: return "Invalid month"
    if day < 1 or day > dayInMonth(month, year): return "Invalid date"
    if len(dtype) != 1 or dtype not in "EQNF": return "Invalid delivery type"
    return ""

packages = []
while True:
    raw = input().strip()
    if raw == "END": break

    iid, dtype, day, month, year = raw.split()
    iid = int(iid)
    day = int(day)
    month = int(month)
    year = int(year)

    error = validate(dtype, day, month, year)
    if error != "":
        print("Error: " + raw + " --> " + error)
    else:
        deliveryDays = {
            "E": 1,
            "Q": 3,
            "N": 7,
            "F": 14,
        }

        newDay = day + deliveryDays[dtype]
        if newDay > dayInMonth(month, year):
            newDay -= dayInMonth(month, year)
            month += 1
        if month > 12:
            month = 1
            year += 1
        
        packages.append([year, month, day, iid])

packages = sorted(packages)

for p in packages:
    print(str(p[3]) + ": delivered on " + str(p[2])+"/"+str(p[1])+"/"+str(p[0]))

    