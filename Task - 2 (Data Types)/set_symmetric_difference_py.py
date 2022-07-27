
#Set .symmetric_difference() Operation

#no of students who have SubScription of English newspaper
n = int(input())
rollNo_1 = set(map(int, input().split()))

#no of students who have SubScription of French newspaper
b = int(input())
rollNo_2 = set(map(int, input().split()))

#students who have subscriptions to English or French newspapers
subscription = rollNo_1.symmetric_difference(rollNo_2)
print(len(subscription))