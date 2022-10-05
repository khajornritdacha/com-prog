n = int(input().strip())

nameToTel = {}
telToName = {}
for _ in range(n):
    raw = input().strip().split()
    nameSurname = raw[0] + " " + raw[1]
    nameToTel[nameSurname] = raw[2]
    telToName[raw[2]] = nameSurname

m = int(input().strip())
for _ in range(m):
    raw = input().strip().split()
    if len(raw) == 1:
        print("{} --> {}".format(raw[0], telToName[raw[0]] if raw[0] in telToName else "Not found"))
    elif len(raw) == 2:
        nameSurname = raw[0] + " " + raw[1]
        print("{} --> {}".format(nameSurname, nameToTel[nameSurname] if nameSurname in nameToTel else "Not found"))
        