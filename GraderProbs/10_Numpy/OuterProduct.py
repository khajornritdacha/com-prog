import numpy as np
def mult_table(nrows, ncols):
    row = np.arange(1, nrows+1).reshape((nrows, 1))
    col = np.arange(1, ncols+1).reshape((1, ncols))
    return np.matmul(row, col)

exec(input().strip()) 