def passReq(x):
    return x[2] == 'A' and x[3] <= 'C' and x[4] <= 'C'

def choose(stu1, stu2):
    if passReq(stu1) and passReq(stu2):
        if float(stu1[1]) > float(stu2[1]):
            return [stu1[0]]
        elif float(stu1[1]) < float(stu2[1]):
            return [stu2[0]]
        elif stu1[3] < stu2[3]:
            return [stu1[0]]
        elif stu1[3] > stu2[3]:
            return [stu2[0]]
        elif stu1[4] < stu2[4]:
            return [stu1[0]]
        elif stu1[4] > stu2[4]:
            return [stu2[0]]
        else:
            return [stu1[0], stu2[0]]
    elif passReq(stu1):
        return [stu1[0]]
    elif passReq(stu2):
        return [stu2[0]]
    else:
        return []

exec(input())
