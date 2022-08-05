import numpy
#user input
arr = input().split()
arr = numpy.array(arr, int)
reshape_arr = numpy.reshape(arr, (3,3))
print(reshape_arr)