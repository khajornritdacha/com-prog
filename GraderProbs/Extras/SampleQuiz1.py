a = int(input())
b = int(input())
c = int(input())

if a < 100:
    while b < c:
        a += b*b + c*c

        if str(a)[-1] == '5':
            break
    
        if a % 2 == 0:
            b += 1
        else:
            c -= 1
        
        if a/(b*c) > 20:
            break
        
else:
    if a < b:
        if b < c:
            a += 3
            b = a + c
            c = b + a
        elif a < c:
            a *= 2
            b = a + b
            c = b + c
        else:
            a = c + a
            b *= 2
            c = b - a
    else:
        if c > a:
            a = 3*b
            b = c+a
            c = a+b
        elif b > c:
            a = b+c
            b = 7*a
            c = b-a
        else:
            a = c-5
            b = a-b
            c = 3*b
    
print(a, b, c)
