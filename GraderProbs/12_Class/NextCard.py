class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "({} {})".format(self.value, self.suit)

    def nextNum(self):
        if self.value == "10": return "J"
        if self.value == "J": return "Q"
        if self.value == "Q": return "K"
        if self.value == "K": return "A"
        if self.value == "A": return "2"
        return int(self.value)+1
        
    def nextSuit(self):
        if self.suit == "club": return "diamond"
        if self.suit == "diamond": return "heart"
        if self.suit == "heart": return "spade"
    
    def next(self):
        if self.value == "2" and self.suit == "spade":
            return Card("3", "club")
        if self.suit == "spade":
            return Card(self.nextNum(), "club")
        return Card(self.value, self.nextSuit())

    def next1(self):
        return self.next()        

    def next2(self):
        newCard = self.next()
        self.value = newCard.value
        self.suit = newCard.suit

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i]) 
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])