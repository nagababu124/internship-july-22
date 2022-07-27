
testCases = int(input())

for _ in range(testCases):
    a = input()
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    print(set_a.issubset(set_b))