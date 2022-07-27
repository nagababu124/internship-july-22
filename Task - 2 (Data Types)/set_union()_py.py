
#Set .union() Operation

#no of students who have SubScription of English newspaper
n = int(input())
rollNo_1 = set(map(int, input().split()))

#no of students who have SubScription of French newspaper
b = int(input())
rollNo_2 = set(map(int, input().split()))

# who atleast have one SubScription
subscription = rollNo_2.union(rollNo_1)
print(len(subscription))