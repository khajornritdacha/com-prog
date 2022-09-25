import random


def genCases():
    MAX = 10000

    n = 100
    res = ""
    nums = [random.randint(1, MAX)*random.choice([1, -1]) for _ in range(n)]
    for cur in nums:
        if cur > 0:
            res += "+" + str(cur)
        else:
            res += str(cur)

    ans = compareAns(res)
    if ans == False:
        print("Fase at case: ")
        print(res)
        exit()

    return ans

def mySol(raw):
    raw = raw.split("+")
    res = 0
    for s in raw:
        cur = s.split("-")
        if cur[0] != "":
            res += int(cur[0])
        
        res += -1*sum(list(map(int, cur[1:])))
    return res

def compareAns(txt):
    return mySol(txt) == eval(txt)


for _ in range(1000):
    genCases()



# print(eval(res))
# print("".join(nums))
