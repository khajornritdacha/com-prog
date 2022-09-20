    op = input().split("2")
    # print(op)

    if op[0] == "str" and op[1] == "RLE":
        raw = input().strip()
        cnt = 0
        for i in range(len(raw)):
            cnt += 1
            if i+1 == len(raw) or raw[i] != raw[i+1]:
                print(raw[i], cnt, end=" ")
                cnt = 0
            
    elif op[0] == "RLE" and op[1] == "str":
        raw = input().strip().split()
        for i in range(0, len(raw), 2):
            char = raw[i]
            rep = int(raw[i+1])

            for j in range(rep):
                print(char, end="")
    else:
        print("Error")
        exit()

