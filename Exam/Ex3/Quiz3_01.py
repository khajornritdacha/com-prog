numTeam = int(input().strip())
teamCoun = {}

for i in range(numTeam):
    raw = input().strip().split()
    teamCoun[raw[0]] = raw[1]

while True:
    raw = input().strip()
    if raw == "q": break

    raw = raw.split()
    ok = True
    countries = set()
    for team in raw:
        if team not in teamCoun:
            ok = False
            break
        countries.add(teamCoun[team])
    
    if len(countries) != len(raw):
        ok = False
    
    if ok: print("OK")
    else: print("Not OK")
