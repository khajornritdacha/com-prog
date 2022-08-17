word = input()
txt = input()

specialChars = "\"(),.\'"
txt = " " + txt + " "
for c in specialChars:
    txt = txt.replace(c, " ")

words = txt.split()
ans = 0
for w in words:
    if w == word:
        ans += 1
print(ans)
