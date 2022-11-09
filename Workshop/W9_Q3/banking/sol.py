def createAccount(acc: dict, accId: str, accName: str, money: float):
    acc[accId] = {
        "name": accName,
        "money": money
    }
    
def invalidTransaction():
    print("Transaction Failed")

def checkExistingAccount(acc, accId, accName):
    return accId in acc and acc[accId]["name"] == accName

def printRes(acc: dict, accId: str):
    money = acc[accId]["money"]
    if money%1 == 0:
        money = int(money)
    print(acc[accId]["name"]+" ("+ accId + ") " + str(money))

numAccounts = int(input().strip())

acc = {}

for _ in range(numAccounts):
    raw = input().strip().split()
    createAccount(acc, raw[1], raw[0], float(raw[2]))

while True:
    raw = input().strip().split()
    if raw[0] == "exit": break

    accName, accId, op = raw[ :3]
    if raw[2] == "deposit":
        money = float(raw[3])
        
        if accId in acc:
            if checkExistingAccount(acc, accId, accName):
                acc[accId]["money"] += money
                printRes(acc, accId)
            else:
                invalidTransaction()
        else:
            createAccount(acc, accId, accName, money)
            printRes(acc, accId)

    elif raw[2] == "withdraw":
        money = float(raw[3])
        if checkExistingAccount(acc, accId, accName) and acc[accId]["money"] >= money:
            acc[accId]["money"] -= money
            printRes(acc, accId)
        else:
            invalidTransaction()
        
    elif raw[2] == "transfer":
        destId = raw[3]
        money = float(raw[4])
        if checkExistingAccount(acc, accId, accName) and destId in acc and acc[accId]["money"] >= money:
            acc[accId]["money"] -= money
            acc[destId]["money"] += money
            printRes(acc, accId)
            printRes(acc, destId)

        else:
            invalidTransaction()
    

