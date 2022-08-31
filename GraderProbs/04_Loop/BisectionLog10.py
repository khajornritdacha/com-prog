def isClose(a, b):
    return abs(a-b) <= 1e-10*max(abs(a), abs(b))

a = float(input())

L = 0
U = a

res = (U+L)/2
while not isClose(a, 10**res):
    if 10**res > a:
        U = res
    else: 
        L = res
    res = (U+L)/2

print(round(res, 6))
