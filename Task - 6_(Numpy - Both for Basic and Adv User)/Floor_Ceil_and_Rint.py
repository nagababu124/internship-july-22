import numpy as np
np.set_printoptions(legacy='1.13')

arr = np.array(input().split(), float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))