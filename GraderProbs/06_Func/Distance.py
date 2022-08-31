import math

def distance1(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def distance2(p1 : list, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])

def distance3(c1, c2):
    d3 = distance1(c1[0], c1[1], c2[0], c2[1])
    epi = 1e-9
    overlap = (max(c1[2], c2[2])-d3 <= epi)
    return d3, overlap

def perimeter(points):
    dis = 0
    prev = points[-1]
    for cur in points:
        dis += distance2(cur, prev)
        prev = cur
    return dis

exec(input().strip())