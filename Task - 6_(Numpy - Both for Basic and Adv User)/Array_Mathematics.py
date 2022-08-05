import numpy as np
#user input
N,M= np.array(input().split(), int)
arr1 = np.array([list(map(int, input().split())) for i in range(N)])
arr2 = np.array([list(map(int, input().split())) for i in range(N)])
#calculation
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(arr1//arr2)
print(np.mod(arr1,arr2))
print(np.power(arr1,arr2))