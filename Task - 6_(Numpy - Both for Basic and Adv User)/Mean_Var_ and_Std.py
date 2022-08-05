import numpy as np
#user input
N,M = map(int,input().split())
arr = np.array([input().split() for _ in range(N)], int)

# mean along with  axis 1(row)
print(np.mean(arr,axis=1))

# variance along axis 0(column)
print(np.var(arr,axis=0))

# Standard deviation along with axis None
print(round(np.std(arr), 11))