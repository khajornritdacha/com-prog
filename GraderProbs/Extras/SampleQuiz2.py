fName = input().strip()
pat = input().strip().lower()
word = input().strip()

with open(fName) as f:
    for raw in f.readlines():
        raw = raw.strip()
        idx = -1
        cur = ""
        ans = ""
        while True:
            try:
                nIdx = raw.index("/", idx+1)
                s = raw[idx+1: nIdx]
                if len(s) == len(pat):
                    same = True
                    for i in range(len(s)):
                        if (pat[i] == s[i].lower() or pat[i] == "?"):
                            same = True
                        else:
                            same = False
                            break
                    if same == True:
                        s = word
                        
                ans += "/" + s
                idx = nIdx
            except:
                break
        
        ans += raw[idx:]
        if idx == -1:
            ans = raw
        else:
            ans = ans[1:]
        print(ans)