import numpy

n,m = map(int,input().split())

my_array = numpy.array([list(map(int,input().split())) for _ in range(n)])
print (numpy.transpose(my_array))
print (my_array.flatten())
