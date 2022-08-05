import numpy as np

N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], int)

# sum of arr along with column
add = np.sum(arr, axis = 0)

# product of sum along with column
product = np.prod(add, axis = 0)

print(product)