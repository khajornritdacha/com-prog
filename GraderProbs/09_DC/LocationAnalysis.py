n = int(input())

towns = []
stuIds = []
for i in range(n):
    newStuId, newTowns = input().split(": ")
    newTowns = (newTowns.split(", "))
    
    stuIds.append(newStuId)
    towns.append(newTowns)

reqId = input()
idx = stuIds.index(reqId)
town = towns[idx]
ans = []

# print(towns)
for i in range(n):
    if i == idx: continue

    matchCnt = 0
    for fiTown in town:
        for c in fiTown:
            if c in towns[i]:
                matchCnt += 1
                break

    if matchCnt > 0:
        ans.append(stuIds[i])

if len(ans) == 0: print("Not Found")
else: print("\n".join(ans))
