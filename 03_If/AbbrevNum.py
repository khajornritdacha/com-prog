n = int(input())

di = ""
deci = 1
deno = 1
  
if (n >= 1e9):
    di = "B"
    deno = 1e9
    if (n >= 1e10):
        deci = 0
        print(str(round(n/deno)) + di)
    else:
        print(str(round(n/deno, deci)) + di)
elif (n >= 1e6):
    di = "M"
    deno = 1e6
    if (n >= 1e7):
        deci = 0
        print(str(round(n/deno)) + di)
    else:
        print(str(round(n/deno, deci)) + di)
elif (n >= 1e3):
    deno = 1e3
    di = "K"
    if (n >= 1e4):
        deci = 0
        print(str(round(n/deno)) + di)
    else:
        print(str(round(n/deno, deci)) + di)
else:
    print(n)
    # print(str(round(n/deno)) + di)
