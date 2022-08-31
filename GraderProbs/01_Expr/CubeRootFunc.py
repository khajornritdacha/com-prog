import math 

def sqrt_n_times(x, n):
 return x ** (1/2**n)

def cube_root(y):
 y = sqrt_n_times(y, 2)
 y *= sqrt_n_times(y, 2)
 y *= sqrt_n_times(y, 4)
 y *= sqrt_n_times(y, 8)
 y *= sqrt_n_times(y, 16)
 y *= sqrt_n_times(y, 32)
 return y
 
def main():
 q = float(input())
 print(cube_root(q))
exec(input()) # DON'T remove this line
