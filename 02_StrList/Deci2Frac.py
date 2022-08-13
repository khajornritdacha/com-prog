# 123.456(789) = (123456 + 789/999) / 1000
# num = 123456
# deno = 999..99 (len of c)

import math

num = input().split(",")

numerator = int(num[0] + num[1])
denominator = 0
tmp = 9
for _ in range(len(num[2])):
    denominator += tmp
    tmp *= 10

# print(numerator)
# print(denominator)

numerator = (numerator*denominator + int(num[2]))
denominator *= (10**len(num[1]))

gc = math.gcd(numerator, denominator)
print(str(numerator//gc) + ' / ' + str(denominator//gc))
