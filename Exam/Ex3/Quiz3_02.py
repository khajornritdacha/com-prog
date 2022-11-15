n, m, k = list(map(int, input().strip().split()))

banditFac = {}
for i in range(n):
    raw = input().strip().split()
    banditFac[raw[0]] = raw[1]

guestFac = {}
for i in range(m):
    raw = input().strip().split()
    guestFac[raw[0]] = set([banditFac[x] for x in raw[1: ]])

for i in range(k):
    raw = input().strip().split()
    commonFac = set(guestFac[raw[0]])
    for guest in raw[1: ]:
        commonFac = commonFac.intersection(guestFac[guest])
    
    if len(commonFac) == 0: print("None")
    else: print( " ".join(sorted(list(commonFac))))

