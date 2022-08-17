raw = input()

cnt = 0
for i in range(len(raw)):
    cnt += 1
    if i == len(raw)-1 or raw[i] != raw[i+1]:
        print(raw[i], cnt, end=" ")
        cnt = 0
    
