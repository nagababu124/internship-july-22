import numpy
# user input
n = list(map(float,input().split()))
m = input();

print(numpy.polyval(n,int(m)))