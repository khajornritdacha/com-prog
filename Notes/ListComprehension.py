def identity( n ):
    return [ [ 1 if i == j else 0 for j in range(n)] for i in range(n)]

def get_peak_indexes(x):
    return [ i for i in range(1, len(x)-1) if(x[i] > x[i-1] and x[i] > x[i+1]) ]

def sum_col(M):
    return [ sum([r[c] for r in M]) for c in range(len(M[0]))]
