op = input()
row = int(input())

raw = ""
col = None
for i in range(row):
    x = input()
    
    if col != None and len(x) != col:
        print("Invalid size")
        exit()

    col = len(x)
    raw += x



def rot90(raw, row, col):
    # (r, c) -> (c, n-r)
    # [r*n + c] -> [c*n + (n-r)]
    ans = list("0"*(row*col))
    for r in range(row):
        for c in range(col):
            ans[c*row + (row-r) - 1] = raw[r*col + c]

    row, col = col, row
    return ans, row, col

ans = list("0"*(row*col))
if op == "90":
    ans, row, col = rot90(raw, row, col)

elif op == "flip":
    for r in range(row):
        for c in range(col):
            ans[r*col + (col-c) - 1] = raw[r*col + c]
            
elif op == "180":
    ans, row, col = rot90(raw, row, col)
    ans, row, col = rot90("".join(ans), row, col)

for r in range(row):
    for c in range(col):
        print(ans[r*col + c], end="")
    print()
