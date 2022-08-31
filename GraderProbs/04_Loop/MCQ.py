ans = input()
stuAns = input()

if len(ans) != len(stuAns):
    print("Incomplete answer")
else:
    score = 0
    for i in range(len(ans)):
        if ans[i] == stuAns[i]:
            score += 1
    print(score)
