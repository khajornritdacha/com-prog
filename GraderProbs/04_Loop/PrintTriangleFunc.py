def print_triangle(h):
    l = h
    r = h
    for row in range(1, h+1):
        for col in range(1, 2*h):
            if (row == h or 
                col == l or
                col == r):
                print("*", end="")
            else:
                print(" ", end="")
        print()
        l -= 1
        r += 1

exec(input()) # DON'T remove this line
