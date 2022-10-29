f1Name = input().strip()
f2Name = input().strip()
with open(f1Name) as colorFile, open(f2Name) as songFile:
    colors2D = [ x.strip().lower().split() for x in colorFile.readlines() ]
    colors = [ x for row in colors2D for x in row]
    # print(colors)

    buffer = ""
    ans = ""
    for x in songFile.read():
        buffer += x
        for color in colors:
            suffix = buffer[len(buffer)-len(color):].lower()
            if suffix == color:
                buffer = buffer[:len(buffer)-len(color)] + "<"+color+">" + buffer[len(buffer)-len(color): ] + "</>"
    
    print(buffer)
