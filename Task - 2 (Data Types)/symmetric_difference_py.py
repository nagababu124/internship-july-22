M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

adef = a.difference(b)
bdef = b.difference(a)

output = adef.union(bdef)

for i in sorted(list(output)):
    print(i)