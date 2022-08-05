import numpy as np
N,M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)],int)

# minimum of  array along with rows
min_arr = np.min(arr, axis=1)

#max_arr of min_arr along with row
print(np.max(min_arr))
