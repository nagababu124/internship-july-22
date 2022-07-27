
#Set .intersection() Operation

#no of students who have SubScription of English newspaper
n = int(input())
rollNo_1 = set(map(int, input().split()))

#no of students who have SubScription of French newspaper
b = int(input())
rollNo_2 = set(map(int, input().split()))

#who have both subscriptions
subscription = rollNo_1.intersection(rollNo_2)
print(len(subscription))