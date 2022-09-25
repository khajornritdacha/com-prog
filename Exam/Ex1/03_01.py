raw = input().split("+")

res = 0
for s in raw:
    cur = s.split("-")
    print(cur)
    if cur[0] != "":
        res += int(cur[0])
    
    res += -1*sum(list(map(int, cur[1:])))

print(res)
# print(raw[0].split("-")[0])
