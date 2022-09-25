def f1(a, b, c):
    tmp = []
    if a > 0:
        tmp.append(a)
    if b > 0:
        tmp.append(b)
    if c > 0:
        tmp.append(c)
    return min(tmp)

def f2(a, b, c):
    tmp = []
    if a < 0:
        tmp.append(a)
    if b < 0:
        tmp.append(b)
    if c < 0:
        tmp.append(c)
    return max(tmp)

def f3(a, b, c):
    return int(str(abs(a+b+c))[0])

def f4(a, b, c):
    return int(str(abs(a+b+c))[-1])
    
def main():
    s1, s2, a, b, c = list(map(int, input().strip().split()))
    if s1 == 0 and s2 == 0:
        print(f1(a, b, c))
    elif s1 == 0 and s2 == 1:
        print(f2(a, b, c))
    elif s1 == 1 and s2 == 0:
        print(f3(a, b, c))
    elif s1 == 1 and s2 == 1:
        print(f4(a, b, c))
    else:
        print("Error")

exec(input().strip()) # DON'T remove this line