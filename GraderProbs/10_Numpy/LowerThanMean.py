import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    scores = weight * data[:, 1:]
    totalScore = np.sum(scores, axis=1)
    mean = np.mean(totalScore)
    failedStudentId = data[totalScore < mean][:, 0]

    if failedStudentId.shape[0] == 0: print("None")
    else: print(", ".join([item for item in failedStudentId.astype(str)]))


exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ