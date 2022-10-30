import numpy as np

def peak_indexes(A):
    A = ((A[1:-1] > A[:-2]) & (A[1:-1] > A[2:]))
    return np.where(A == True)[0] + 1


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())
