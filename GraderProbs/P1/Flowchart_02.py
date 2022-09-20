n, k = map(int, input().split())

if n%2 == 1:
    sum_a = 0
    sum_b = 0
    sum_c = 0
    m = 0

    while m < k:
        a, b, c = map(int, input().split())
        if a == b:
            if b == c:
                if a+b > k:
                    sum_a += 1
                    sum_b += 2
                    sum_c -= 3
                else:
                    sum_a -= 3
                    sum_b -= 2
                    sum_c += 1
            else:
                sum_a += 2
                sum_b -= 3
        m += 1

    print(sum_a, sum_b, sum_c)
else:
    s, t = map(int, input().split())

    x = s
    y = t
    if s > t:
        x = s-t
    elif s < t:
        y = 2*(t-s)
    
    if x+y > k:
        x, y = y, x
        x = y + s*s

    print(x, y)