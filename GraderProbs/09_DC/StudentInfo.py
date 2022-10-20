from string import ascii_uppercase

n = int(input())
students = [input().split() for i in range(n)]
req = input().split()

students = sorted(students, key=lambda x: x[0])
# print(students)

ans = []
for idx, data in enumerate(students):
    chk = 0
    for i in range(len(req)):
        if req[i].isnumeric():
            chk += (req[i] == data[2])
        elif req[i] in ascii_uppercase or req[i] == "Dog":
            chk += (req[i] == data[1])
        else:
            chk += (req[i] == data[3])
            
    if chk == len(req):
        ans.append(data)

if len(ans) == 0: print("Not Found")
else: print("\n".join([ " ".join(x) for x in ans]))
