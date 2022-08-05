import numpy
numpy.set_printoptions(legacy = '1.13')
array_size = numpy.array(input().split(), int)
print(numpy.eye(array_size[0],array_size[1],k=0))
#print(array_size)