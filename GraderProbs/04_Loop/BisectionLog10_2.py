def isClose(a, b):
    return abs(a-b) <= 1e-10*max(abs(a), abs(b))

a = float(input())

def estimateUpB(x):
    cnt = 0
    while x > 1:
        x /= 10
        cnt += 1
    return cnt + 1

L = 0
U = estimateUpB(a)

res = (U+L)/2
while not isClose(a, 10**res):
    if 10**res > a:
        U = res
    else: 
        L = res
    res = (U+L)/2

print(round(res, 6))
