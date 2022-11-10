# Date: 10 Nov 2022
# Time: 11.52 min

numDocs = int(input().strip())
docs = dict()
for i in range(numDocs):
    docName = input().strip()
    details = input().strip().split()
    docs[docName] = details

def calculateScore(docs, word):
    order = []
    for docName, text in docs.items():
        freq = text.count(word) / len(text)
        specific = 1 / len(set(text))
        relatedScore = freq * specific
        order.append([relatedScore, docName])
    mx = max(order, key=lambda x: x[0])
    if mx[0] == 0: return "0"
    return mx[1]

while True:
    raw = input().strip()
    if raw == "-1": break

    docName = calculateScore(docs, raw)
    if docName == "0": print("NOT FOUND")
    else: print(docName)
    