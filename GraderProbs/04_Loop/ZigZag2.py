zig = 0
zag = 1
first = True

while 1:
    raw = input()
    if raw == "Zig-Zag":
        print(mnZig, mxZag)
        break
    elif raw == "Zag-Zig":
        print(mnZag, mxZig)
        break

    raw = list(map(int, raw.split()))
    if first:
        mnZig = raw[zig]
        mxZig = raw[zig]
        mnZag = raw[zag]
        mxZag = raw[zag]
        first = False
    
    mnZig = min(raw[zig], mnZig)
    mxZig = max(raw[zig], mxZig)
    mnZag = min(raw[zag], mnZag)
    mxZag = max(raw[zag], mxZag)

    zig = 1-zig
    zag = 1-zag
    
