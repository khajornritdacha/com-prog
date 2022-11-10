import numpy as np

fileName = input().strip()
op = input().strip()
OPERATIONS = ["LSTRIP", "RSTRIP", "STRIP", "STRIP_ALL"]

sumValidCharacter = lambda arr: np.sum((arr != "."), axis=0) 

def leftStrip(arr):
    sumChars = sumValidCharacter(arr)
    i = 0
    while i < arr.shape[1]:
        if sumChars[i] != 0:
            break
        i += 1
    return arr[:, i:]

def rightStrip(arr):
    arr = arr[:, ::-1]
    sumChars = sumValidCharacter(arr)
    i = 0
    while i < arr.shape[1]:
        if sumChars[i] != 0:
            break
        i += 1
    return arr[:, i:][:, ::-1]

def insideStrip(arr):
    sumChars = sumValidCharacter(arr)
    validChars = []
    i = 0
    while i < arr.shape[1]:
        if sumChars[i] > 0:
            validChars.append(i)
        i += 1
    return arr[:, validChars]

with open(fileName, "r") as file:
    if op not in OPERATIONS:
        print("Invalid command")
        exit(0)
    
    arr = np.array([ list(raw.strip()) for raw in file])

    if op != "RSTRIP":
        arr = leftStrip(arr)
    
    if op != "LSTRIP":
        arr = rightStrip(arr)
    
    if op == "STRIP_ALL":
        arr = insideStrip(arr)
    
    print("\n".join(["".join(x) for x in arr]))
