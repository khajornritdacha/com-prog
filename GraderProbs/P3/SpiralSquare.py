def spiral_square(n): # n is a positive odd number
    arr = [ [ 0 for c in range(n) ] for r in range(n) ]

    r = n-1
    c = n-1
    dr = 0
    dc = -1
    num = n*n

    while True:

        assert(r >= 0 and c >= 0 and r <= n-1 and c <= n-1)

        arr[r][c] = num
        num -= 1

        if num == 0: break

        if dc == -1 and (c+dc < 0 or arr[r][c+dc] != 0):
            r -= 1
            dr = -1
            dc = 0
        elif dc == 1 and (c+dc > n-1 or arr[r][c+dc] != 0) :
            r += 1
            dr = 1
            dc = 0
        elif dr == -1 and (r+dr < 0 or arr[r+dr][c] != 0):
            c += 1
            dr = 0
            dc = 1
        elif dr == 1 and (r+dr > n-1 or arr[r+dr][c] != 0):
            c -= 1
            dr = 0
            dc = -1
        else:
            r += dr
            c += dc

    return arr

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip()) 