# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()

arr = input().split()

A = set(input().split())
B = set(input().split())
count = 0
for i in arr:
    if i in A:
        count = count+1
    if i in B:
        count = count-1

print(count)