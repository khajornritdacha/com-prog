def factor(N): # N เป็ นจ ำนวนเต็มบวกมำกกว่ำ 1
    res = []
    for i in range(2, N+1):
        if i*i > N:
            break

        count = 0
        while N%i == 0:
            count += 1
            N //= i
            # print(N, i)

        if count > 0:
            res.append([i, count])
    
    if N > 1:
        res.append([N, 1])
    return res

exec(input().strip())
