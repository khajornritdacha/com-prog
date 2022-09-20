n = int(input())

data = [] # (dis, x, y, idx)

def distance(x, y):
    return ((x**2) + (y**2))**0.5

def cmp(x):
    return x[0]

for i in range(n):
    raw = list(map(float, input().split()))
    data.append([distance(raw[0], raw[1]), raw[0], raw[1], i+1])

data.sort(key = cmp)

print("#{}: ({}, {})".format(data[2][3], data[2][1], data[2][2]))
