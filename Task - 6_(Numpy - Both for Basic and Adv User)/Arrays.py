import numpy

def arrays(arr):
    arr2 = numpy.array(arr, float)
    # print the array in the reverse order
    return arr2[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)