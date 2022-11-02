scores = dict()
votedBy = dict()
fanData = dict()

while True:
    raw = input().strip().split()
    if len(raw) == 1:
        winners = ["", "", ""]
        if raw[0] == "1":
            scoresList = sorted(list(scores.values()), reverse=True)
            for name, score in scores.items():
                for i in range(len(winners)):
                    if score == scoresList[i]:
                        assert winners[i] == ""
                        winners[i] = name
        elif raw[0] == "2":
            scoresList = sorted(list(map(len, votedBy.values())), reverse=True)
            for name, votes in votedBy.items():
                for i in range(len(winners)):
                    if len(votes) == scoresList[i]:
                        assert winners[i] == ""
                        winners[i] = name
        elif raw[0] == "3":
            numKamiOshi = dict()
            for fanName, data in fanData.items():
                mxScore = max(data.values())
                kamiOshi = ""
                for idolName, score in data.items():
                    if idolName not in numKamiOshi: numKamiOshi[idolName] = 0
                    if score == mxScore and (kamiOshi == "" or idolName < kamiOshi):
                        kamiOshi = idolName
                
                numKamiOshi[kamiOshi] += 1
            
            scoresList = sorted(list(numKamiOshi.values()), reverse=True)
            for name, score in numKamiOshi.items():
                for i in range(len(winners)):
                    if score == scoresList[i]:
                        assert winners[i] == ""
                        winners[i] = name

        
        print(", ".join(winners))
        break

    fanName = raw[0]
    idolName = raw[1]
    vote = int(raw[2])

    if idolName not in scores:
        scores[idolName] = 0
        votedBy[idolName] = set()

    if fanName not in fanData:
        fanData[fanName] = dict()
    
    if idolName not in fanData[fanName]:
        fanData[fanName][idolName] = 0

    scores[idolName] += vote
    votedBy[idolName].add(fanName)
    
    fanData[fanName][idolName] += vote

