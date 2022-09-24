def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split() # ลบ blank ซ้ายขวา
        if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", "" # แฟ้มหมดแล้ว คืนสตริงว่าง

fileNames = input().strip().split()

with open(fileNames[0]) as f1, open(fileNames[1]) as f2:
    s1Id, s1G = read_next(f1)
    s2Id, s2G = read_next(f2)

    while True:    
        if s1Id == "" and s2Id == "":
            break

        win = 1
        if s1Id == "":
            win = 2
        elif s2Id == "":
            win = 1
        else:
            fac1Id = s1Id[-2:]
            fac2Id = s2Id[-2:]

            if fac1Id < fac2Id:
                win = 1
            elif fac2Id < fac1Id:
                win = 2
            elif s1Id < s2Id:
                win = 1
            elif s2Id < s1Id:
                win = 2
        
        assert win == 1 or win == 2

        if win == 1:
            print(s1Id, s1G)
            s1Id, s1G = read_next(f1)
        elif win == 2:
            print(s2Id, s2G)
            s2Id, s2G = read_next(f2)
