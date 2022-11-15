couAlly = {}
couEnem = {}

def addEnemy(couEnem: dict, couAlly: set, enemAlly: set):
    for cou in couAlly:
        if cou not in couEnem: couEnem[cou] = set()
        couEnem[cou].update(enemAlly)
    return couEnem

while True:
    raw = input().strip().split()
    if raw[0] == "End": break

    if raw[0] == "Ally":
        for coun in raw[1: ]:
            tmp = set(raw[1: ])
            couAlly[coun] = tmp
        
    elif raw[0] == "Enemy":
        if raw[1] not in couAlly: couAlly[raw[1]] = set([raw[1]])
        if raw[2] not in couAlly: couAlly[raw[2]] = set([raw[2]])

        couEnem = addEnemy(couEnem, couAlly[raw[1]], couAlly[raw[2]])
        couEnem = addEnemy(couEnem, couAlly[raw[2]], couAlly[raw[1]])
    elif raw[0] == "Table":
        raw.append(raw[1])
        ok = True
        for i in range(1, len(raw)-1):
            if raw[i] in couEnem and raw[i+1] in couEnem[raw[i]]:
                ok = False
    
        if ok: print("Okay")
        else: print("No")
        
    
