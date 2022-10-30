import numpy as np

def sum_2_rows( M ):
    R, C = M.shape
    return np.array([M[r] + M[r+1] for r in range(0, R, 2)])

def sum_left_right( M ):
    R, C = M.shape  
    return M[:, :C//2] + M[:, C//2:] 


def sum_upper_lower( M ):
    R, C = M.shape
    return M[:R//2] + M[R//2:]

def sum_4_quadrants( M ):
    R, C = M.shape
    return M[:R//2, :C//2] + M[:R//2, C//2:] + M[R//2:, :C//2] + M[R//2:, C//2:]

def sum_4_cells( M ):
    return M[::2, ::2] + M[1::2, ::2] + M[::2, 1::2] + M[1::2, 1::2]

def count_leap_years( years ):
    # years เป็นอาเรย์เก็บปี พ.ศ.
    # คืนจ านวนปีใน years ที่เป็นปีอทิกสุรทิน (ปีที่ ก.พ. มี 29 วัน)
    years -= 543
    return np.sum((years%400 == 0) | ((years%4 == 0) & (years%100 != 0)))

exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
