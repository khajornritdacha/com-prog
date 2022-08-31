a = input().split()
b = input().split()

def passReq(x):
    return x[2] == 'A' and x[3] <= 'C' and x[4] <= 'C'

if passReq(a) and passReq(b):
    if float(a[1]) > float(b[1]):
        print(a[0])
    elif float(a[1]) < float(b[1]):
        print(b[0])
    elif a[3] < b[3]:
        print(a[0])
    elif a[3] > b[3]:
        print(b[0])
    elif a[4] < b[4]:
        print(a[0])
    elif a[4] > b[4]:
        print(b[0])
    else:
        print("Both")
elif passReq(a):
    print(a[0])
elif passReq(b):
    print(b[0])
else:
    print("None")
