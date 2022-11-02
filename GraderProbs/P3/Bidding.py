n = int(input().strip())
bidder = dict()
price = dict()
winners = dict()

def removeBidder(userId, productId, bidder, price):
    if productId in bidder and userId in bidder[productId]:
        preIdx = bidder[productId].index(userId)
        bidder[productId].pop(preIdx)
        price[productId].pop(preIdx)

for _ in range(n):
    raw = input().strip().split()
    if raw[0] == "B":
        raw[3] = int(raw[3])
        if raw[1] not in winners:
            winners[raw[1]] = [0, []]

        if raw[2] not in bidder:
            bidder[raw[2]] = []
            price[raw[2]] = []
        
        removeBidder(raw[1], raw[2], bidder, price)
        
        # Insert new element
        newIdx = -1
        for i in range(len(bidder[raw[2]])):
            if price[raw[2]][i] > raw[3]:
                newIdx = i
                break 
        
        if newIdx == -1: newIdx = len(bidder[raw[2]])
        bidder[raw[2]].insert(newIdx, raw[1])
        price[raw[2]].insert(newIdx, raw[3])

    elif raw[0] == "W":
        removeBidder(raw[1], raw[2], bidder, price)

for productId, data in bidder.items():
    mx = -1
    winIdx = -1
    for i in range(len(data)):
        bid = data[i]
        pri = price[productId][i]

        if pri > mx:
            mx = pri
            winIdx = i
    
    if winIdx > -1:
        winners[data[winIdx]][0] += price[productId][winIdx]
        winners[data[winIdx]][1].append(productId)

for userId in sorted(list(winners.keys())):
    print("{}: ${}".format(userId, winners[userId][0]), end="")
    if len(winners[userId][1]) > 0:
        winners[userId][1].sort()
        print(" -> {}".format(" ".join(winners[userId][1])))
    else:
        print()

