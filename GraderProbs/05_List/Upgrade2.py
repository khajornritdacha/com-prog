ids = []
grades = []
while True:
    x = input().strip().split()
    if x[0] == "q":
        break

    ids.append(x[0])
    grades.append(x[1])

uids = input().strip().split()

for uid in uids:
    idx = ids.index(uid)
    
    x = grades[idx]
    res = "A"
    if x == "B+":
        res = "A"
    elif x == "B":
        res = "B+"
    elif x == "C+":
        res = "B"
    elif x == "C":
        res = "C+"
    elif x == "D+":
        res = "C"
    elif x == "D":
        res = "D+"
    elif x == "F":
        res = "D"
    grades[idx] = res

stuDatas = [(ids[i], grades[i]) for i in range(len(ids))]
stuDatas.sort()

for x, y in stuDatas:
    print(x, y)
