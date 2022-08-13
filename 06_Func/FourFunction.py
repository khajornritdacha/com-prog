def make_int_list(x):
    return list(map(int, x.split()))

def is_odd(e):
    return (e%2 != 0)

def odd_list(alist):
    return [i for i in alist if is_odd(i)]

def sum_square(alist):
    return sum([i**2 for i in alist])

exec(input().strip())
