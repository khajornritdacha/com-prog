# arr1 = input()[1:-1].split(',')
arr1 = [float(i) for i in input()[1:-1].split(',')]
arr2 = [float(i) for i in input()[1:-1].split(',')]
arr3 = [arr1[i] + arr2[i] for i in range(len(arr1))]
print(arr1, end="")
print(' + ', end="")
print(arr2, end="")
print(' = ', end="")
print(arr3)