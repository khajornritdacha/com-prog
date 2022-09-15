raw = input().strip().upper()
op = input().strip()

dnaPairs = {
    "A" : "T",
    "T" : "A",
    "G" : "C",
    "C" : "G",
}

if op == "R":
    ans = ""
elif op == "F":
    ans = {}
elif op == "D":
    pat = input().strip()
    ans = 0
else:
    assert(0)

for i in range(len(raw)):
    if raw[i] not in dnaPairs:
        print("Invalid DNA")
        quit()

    if op == "R":
        ans += dnaPairs[raw[i]]
    elif op == "F":
        if raw[i] not in ans:
            ans[raw[i]] = 0
        ans[raw[i]] += 1
    elif op == "D":
        if i+1 < len(raw) and raw[i] == pat[0] and raw[i+1] == pat[1]:
            ans += 1

if op == "R":
    ans = ans[::-1]
    print(ans)
elif op == "F":
    print("A={}, T={}, G={}, C={}".format(ans['A'], ans['T'], ans['G'], ans['C']))
elif op == "D":
    print(ans)

