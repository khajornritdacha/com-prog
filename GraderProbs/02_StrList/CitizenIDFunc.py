def check_digit(n):
    s = 0
    for i in range(0, len(n[:12])):
        s += (13-i) * int(n[i])
    s = (11 - (s % 11)) % 10
    return s

exec(input()) # DON'T remove this line
