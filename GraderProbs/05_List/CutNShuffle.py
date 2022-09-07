cards = input().split()
ops = input()

def cut(arr):
    return arr[len(arr)//2:] + arr[:len(arr)//2]

def sli(arr):
    li1 = arr[:len(arr)//2]
    li2 = arr[len(arr)//2:]
    res = []
    for i in range(len(li1)):
        res.append(li1[i])
        res.append(li2[i])
    return res

for op in ops:
    if op == "C":
        cards = cut(cards)
    elif op == "S":
        cards = sli(cards)

print(" ".join(cards))
