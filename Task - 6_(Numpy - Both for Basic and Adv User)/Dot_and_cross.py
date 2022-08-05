import numpy as np
#user input
N = int(input())
arr1 = np.array([input().split() for _ in range(N)], int)
arr2 = np.array([input().split() for _ in range(N)], int)

print(np.dot(arr1,arr2))