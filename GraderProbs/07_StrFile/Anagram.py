# s1 = list(input().strip().lower())
# s2 = list(input().strip().lower())
s1 = [ c for c in input().strip().lower() if c.isalpha() ]
s2 = [ c for c in input().strip().lower() if c.isalpha() ]

s1.sort(reverse=True)
s2.sort(reverse=True)

# print(s1)
# print(s2)

isAnagram = (len(s1) == len(s2))
for c1, c2 in zip(s1, s2):
    if c1 != c2:
        isAnagram = False
        break

if isAnagram:
    print("YES")
else:
    print("NO")



