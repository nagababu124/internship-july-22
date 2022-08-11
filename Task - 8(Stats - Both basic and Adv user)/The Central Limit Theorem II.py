# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

num_tic = float(input())
num_students = float(input())
mu = num_students * float(input())
sigma = math.sqrt(num_students) * float(input())

print(round(0.5*(1+math.erf((num_tic - mu)/(sigma * math.sqrt(2)))),4))