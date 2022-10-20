n = int(input().strip())

union = set()
intersect = set()

for i in range(n):
    raw = set(map(int, input().strip().split()))
    if i == 0:
        union = raw.copy()
        intersect = raw.copy()        
    union = union.union(raw)
    intersect = intersect.intersection(raw)

print(len(union))
print(len(intersect))
