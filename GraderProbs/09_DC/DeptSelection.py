majorNum = int(input())
major = dict()
for i in range(majorNum):
    raw = input().split()
    major[raw[0]] = int(raw[1])

studentNum = int(input())
students = [ input().split() for i in range(studentNum) ]
students = sorted(students, key=lambda x: float(x[1]), reverse=True)
# print(students)

studentMajor = dict()
for data in students:
    for i in range(2, len(data)):
        if major[data[i]] > 0:
            major[data[i]] -= 1
            studentMajor[data[0]] = data[i]
            break
    
for key in sorted(studentMajor):
    print(key, studentMajor[key])
