from math import floor


data = []
sumFixStroke = 0
sumPar = 0
sumStroke = 0

for _ in range(9):
    x = list(map(int, input().strip().split()))
    x.append( min(x[1], x[0]+2) )
    
    if x[2] == 1:
        sumFixStroke += x[3]
    
    sumPar += x[0]
    sumStroke += x[1]


bonusScore = floor(0.8*(sumFixStroke*1.5 - sumPar))
score = sumStroke - bonusScore

print(sumStroke)
print(bonusScore)
print(score)



