numWeek = int(input().strip())

def calculateEMA(prices: list, period: int) -> list:
    # Calculate e(t0)
    
    if len(prices) < period: return [] 

    e = [1.0/period*sum(prices[:period])] 
    alpha = 2.0/(1+period)

    for i in range(period, len(prices)):
        curEma = alpha * prices[i] + e[-1] * (1-alpha)
        e.append(curEma)

    return e

def findIntersection(slowEma: list, fastEma: list) -> list:
    res = []

    assert len(fastEma) > len(slowEma)

    fastEma = fastEma[len(fastEma)-len(slowEma): ]
    for i in range(len(slowEma)-1):
        if slowEma[i] < fastEma[i] and slowEma[i+1] > fastEma[i+1]:
            # print(f"{slowEma[i]} {fastEma[i]} {slowEma[i+1]} {fastEma[i+1]}")
            res.append(f"SELL at {prices[14+i]}")
            if prices[14+i]%1 == 0: res[-1] += "0"
        
        if slowEma[i] > fastEma[i] and slowEma[i+1] < fastEma[i+1]:
            res.append(f"BUY at {prices[14+i]}")
            if prices[14+i]%1 == 0: res[-1] += "0"
    

    return res


prices = []
FASTPERIOD = 7
SLOWPERIOD = 14

for _ in range(numWeek):
    prices += list(map(float, input().strip().split(",")))

slowEMA = calculateEMA(prices, SLOWPERIOD)
fastEMA = calculateEMA(prices, FASTPERIOD)

res = findIntersection(slowEMA, fastEMA)

if len(res) == 0: print("No results")
else: print("\n".join(res))


