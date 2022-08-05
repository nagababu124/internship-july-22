import numpy as np
#user input
arr1 = np.array(input().split(),int)
arr2 = np.array(input().split(),int)

#inner product of two arrays
print(np.inner(arr1, arr2))

#outer product of two arrays
print(np.outer(arr1, arr2))