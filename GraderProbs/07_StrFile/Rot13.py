import string

while True:
    raw = input().strip()
    if raw == "end":
        break
    for r in raw:
        if r.isalpha():
            isUpper = r.isupper()
            r = r.lower()
            r = string.ascii_lowercase[ (string.ascii_lowercase.index(r) + 13) % len(string.ascii_lowercase) ]
            if isUpper:
                r = r.upper()
        print(r, end="")
    print()