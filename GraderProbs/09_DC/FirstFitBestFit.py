def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for arr in L:
        if sum(arr) + e <= 100:
            arr.append(e)
            return
    L.append([e])
    return

def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    mnDif = 100000
    mnIdx = -1
    for idx, arr in enumerate(L):
        dif = 100 - sum(arr) - e
        if dif >= 0 and dif < mnDif:
            mnIdx = idx
            mnDif = dif

    if mnIdx != -1:
        L[mnIdx].append(e)
    else:
        L.append([e])
    return

def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    res = []
    for v in D:
        first_fit(res, v)
    return res

def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    res = []
    for v in D:
        best_fit(res, v)
    return res

exec(input().strip())