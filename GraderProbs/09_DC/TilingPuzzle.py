def row_number(t, e): # return row number of t containing e (top row is row #0)
    for r, row in enumerate(t):
        for v in row:
            if v == e:
                return r
    assert(False)
    return -1

def flatten(t): # return a list of ints converted from list of lists of ints t
    return [v for row in t for v in row if v != 0]

def inversions(x): # return the number of inversions of list x    
    return sum([1 for l in range(len(x)) for r in range(l+1, len(x)) if x[l] > x[r]])

def solvable(t): # return True if tiling t (list of lists of ints) is solvable
 # otherwise return False
    flattenedT = flatten(t)
    if len(t)%2 != 0 and inversions(flattenedT)%2 == 0:
        return True
    elif len(t)%2 == 0 and inversions(flattenedT)%2 != 0 and row_number(t, 0)%2 == 0:
        return True
    elif len(t)%2 == 0 and inversions(flattenedT)%2 == 0 and row_number(t, 0)%2 != 0:
        return True

    return False


exec(input().strip()) # do not remove this line
