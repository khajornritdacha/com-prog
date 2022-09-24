raw = input().strip()

word = ""
ans = ""
for idx, c in enumerate(raw):
    if c.isalnum():
        word += c

        if idx+1 == len(raw) or raw[idx+1].isalnum() == False:
            tmp = word.lower()
            if len(ans) != 0:
                tmp = word.capitalize()
            ans += tmp
            word = ""

print(ans)   
