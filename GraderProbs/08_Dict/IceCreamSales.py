# max_dict = {'Australia':178, 'Germany':213, 'Japan': 867}
# print("Japan" in max_dict)
# print(max(max_dict.values()))

n = int(input().strip())
iceCreams = {}
for _ in range(n):
    raw = input().strip().split()
    iceCreams[raw[0]] = float(raw[1])

m = int(input().strip())
ordered = {}
total = 0
for _ in range(m):
    raw = input().strip().split()
    if raw[0] in iceCreams:
        cur = float(raw[1]) * iceCreams[raw[0]]
        total += cur
        if raw[0] not in ordered:
            ordered[raw[0]] = 0
        ordered[raw[0]] += cur
    

if total == 0:
    print("No ice cream sales")
else:
    mx = max(ordered.values())
    topSales = [name for name, sales in ordered.items() if sales == mx]
    topSales.sort()
    print("Total ice cream sales: {}".format(total))
    print("Top sales: {}".format(", ".join(topSales)))

    

