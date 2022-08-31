code = input()
one = ""
two = ""
for i in range(3, len(code), 7):
    one += code[i]
for i in range(7, len(code), 5):
    two += code[i]

# print(one)
# print(two)

three = int(one) + int(two) + 10000
four = str(three)[-4: -1]

sum = 0
for c in four:
    sum += int(c)

# print(four)
# print(sum)
# print(str(sum)[-1:])

lastDigit = int(str(sum)[-1:]) + 1
# print(lastDigit)
print(four + chr(lastDigit + 65 - 1))