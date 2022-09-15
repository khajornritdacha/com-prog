import math

def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def distance2(p1 : list, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])

def distance3(c1, c2):
    d3 = distance2(c1[: 2], c2[: 2])
    overlap = (c1[2] + c2[2] >= d3)
    return d3, overlap
    

def perimeter(points):
    dis = 0
    for i in range(len(points)):
      dis += distance2(points[i], points[ (i+1) % len(points) ])
    return dis

exec(input().strip())
