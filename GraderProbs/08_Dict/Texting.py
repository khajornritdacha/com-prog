from string import ascii_lowercase as lowLet

keyTextDi = {}
textKeyDi = {}
cnt = 0
num = 1
for idx, char in enumerate(lowLet):
    if char in "adgjmptw":
        cnt = 0
        num += 1
    cnt += 1

    key = str(num) * cnt
    textKeyDi[char] = key
    keyTextDi[key] = char

textKeyDi[" "] = "0"
keyTextDi["0"] = " "
# print(textKeyDi)
# print(keyTextDi)

def text2keys( text ):
    text = text.lower()    
    res = []
    for c in text:
        if c in textKeyDi:
            res += [textKeyDi[c]]
    return " ".join(res)

def keys2text( keys ):
    keys = keys.strip().split()
    res = ""
    for c in keys:
        res += keyTextDi[c]
    return res

exec(input().strip())