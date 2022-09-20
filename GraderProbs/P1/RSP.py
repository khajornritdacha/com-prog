rounds = int(input().strip())

OPS = ["R", "S", "P"]
score = [0, 0]

def index(char, step = 0):
    return (OPS.index(char) + step)%3

for rnd in range(3 * rounds):
    raw = input().strip().split()
    
    winner = None
    if OPS[index(raw[0], 1)] == OPS[index(raw[1])]:
        winner = 0
    elif OPS[index(raw[1], 1)] == OPS[index(raw[0])]:
        winner = 1

    if winner != None:
        score[winner] += 1
        if score[winner] == rounds:
            print(score[0], score[1])
            print("Player {} wins".format(winner+1))
            exit()

        
print(score[0], score[1])
print("Tie")
