with open("in1.txt") as f:
    # read the entire file as one string
    print(f.read())
    # read first 5 characters
    print(f.read(5))

    # read line by line
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

    # loop through each line of the file
    for x in f:
        print(x)
