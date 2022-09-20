months = """January
February
March
April
May
June
July
August
September
October
November
December""".split()

def getInput():
    p1 = input().split()
    p1[1] = months.index(p1[1]) + 1
    p1[2] = int(p1[2][:-1])
    p1[3] = int(p1[3])
    return p1

p1 = getInput()
p2 = getInput()

if p1[1: ] == p2[1:]:
    print(p1[0], p2[0])
else:
    ans = p1[0]
    if p2[3] < p1[3] \
    or (p2[3] == p1[3] and p2[1] < p1[1]) \
    or (p2[3] == p1[3] and p2[1] == p1[1] and p2[2] < p1[2]):
        ans = p2[0]
    
    print(ans)

# print(p1, p2)