numOp = int(input().strip())

calculateRating = lambda l, s: int(25*(l+1)*(s/(1e7)))

songData = dict()
for _ in range(numOp):
    raw = input().strip().split(" | ")
    if raw[0] == "Play":
        raw[2], raw[3] = int(raw[2]), int(raw[3])
        curRating = calculateRating(raw[2], raw[3])
        curData = [curRating, raw[2], raw[3]]
        if raw[1] not in songData:
            songData[raw[1]] = curData
            
        if curRating > songData[raw[1]][0]:
            songData[raw[1]] = curData
        elif curRating == songData[raw[1]][0] and raw[2] > songData[raw[1]][1]:
            songData[raw[1]] = curData
        elif curRating == songData[raw[1]][0] and raw[2] == songData[raw[1]][1] and raw[3] > songData[raw[1]][2]:
            songData[raw[1]] = curData
    elif raw[0] == "Rating" and len(raw) > 1:
        if raw[1] not in songData:
            print(0)
        else:
            print(songData[raw[1]][0])
    elif raw[0] == "Rating":
        playerRating = sum(sorted([rating[0] for rating in songData.values()], reverse=True)[: 5])
        print(playerRating)
    elif raw[0] == "Detail":
        if raw[1] not in songData:
            print(raw[1] + ": No play history")
        else:
            print(raw[1] + " | " + str(songData[raw[1]][1]) + " | " + str(songData[raw[1]][2]) + " | " + str(songData[raw[1]][0]))