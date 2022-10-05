def total(pocket):
    return sum([k*v for k, v in pocket.items()])

def take(pocket, money_in):
    for k, v in money_in.items():
        if k not in pocket:
            pocket[k] = 0
        pocket[k] += v

def pay(pocket, amt):
    paid = {}
    for k, v in sorted(pocket.items(), reverse=True):
        reqNote = amt//k
        paidAmt = min(reqNote, v)
        v -= paidAmt
        amt -= paidAmt * k
        if paidAmt > 0:
            paid[k] = paidAmt
    
    if amt > 0:
        return {}
    
    for k, v in paid.items():
        pocket[k] -= v
    return paid

exec(input().strip())
