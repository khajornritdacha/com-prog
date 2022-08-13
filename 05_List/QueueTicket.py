n = int(input())

lastFin = -1
cus = []
avgSum = 0
finCnt = 0

for _ in range(n):
    op = input().split()
    if op[0] == "reset":
        curQ = int(op[1])
    elif op[0] == "new":
        print("ticket " + str(curQ))
        cus.append([curQ, int(op[1])])
        curQ += 1
    elif op[0] == "next":
        lastFin += 1
        print("call " + str(cus[lastFin][0]))
    elif op[0] == "order":
        t = int(op[1])
        dt = t - cus[lastFin][1]
        avgSum += dt
        finCnt += 1
        print("qtime", str(cus[lastFin][0]), dt)
    elif op[0] == "avg_qtime":
        print("avg_qtime", round(avgSum / finCnt, 4))
