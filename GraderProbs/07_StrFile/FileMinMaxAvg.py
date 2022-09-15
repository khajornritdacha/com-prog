raw = input().strip().split()
reqCode = raw[1][-2: ]


students = []
with open(raw[0], "r") as file:
    while True:
        x = file.readline().strip().split()
        if not x:
            break

        curCode = x[0][:2]

        if curCode == reqCode:
            students.append(float(x[1]))

if len(students) == 0:
    print("No data")
else:
    print("{} {} {}".format(min(students), max(students), sum(students)/len(students)))
