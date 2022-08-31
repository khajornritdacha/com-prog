import math

PI = math.pi

n = int(input())

fTerm = math.sqrt(2*PI)
sTerm = pow(n, n+1/2)
tTermL = pow(math.e, -n + (1 / (12*n+1) ))
tTermU = pow(math.e, -n + (1 / (12*n) ))


low = fTerm * sTerm * tTermL
up = fTerm * sTerm * tTermU
print(low)
print(up)



