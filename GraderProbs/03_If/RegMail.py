weight = int(input())

if weight <= 100:
    print(18)
elif weight <= 250:
    print(22)
elif weight <= 500:
    print(28)
elif weight <= 1000:
    print(38)
elif weight <= 2000:
    print(58)
else:
    print("Reject")
