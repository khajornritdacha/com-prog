raw = input().strip()
op = int(input().strip())

curFrame = 1
frameData = []

i = 0
while i < len(raw):
    if curFrame == 10:
        frameData.append(raw[i:])
        break
    else:
        if raw[i] == "X":
            frameData.append(raw[i])
        else:
            frameData.append(raw[i: i+2])
            i += 1

    curFrame += 1        
    i += 1

def getScore(x, k):
    if x[k] == "X":
        return 10
    elif x[k] == "/":
        return 10 - int(x[k-1])
    else:
        return int(x[k])

def calScore(frameData, idx, LIM):
    k = 0
    cnt = 0 
    score = 0
    while cnt < LIM:
        score += getScore(frameData[idx], k)
        k += 1
        if k == len(frameData[idx]):
            idx += 1
            k = 0
        cnt += 1
    
    return score

frameScore = []
for i in range(len(frameData)):
    score = 0
    step = 2

    if i == len(frameData)-1:
        step = len(frameData[i])
    elif frameData[i] == "X" or frameData[i][1] == "/":
        step = 3

    score = calScore(frameData, i, step)
    frameScore.append(score)


if 1 <= op <= 10:
    print(frameScore[op-1])
else:
    print(sum(frameScore))

