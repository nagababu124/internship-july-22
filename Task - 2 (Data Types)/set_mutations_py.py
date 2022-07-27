
# n for number of elements in set A
n = int(input())

# set_A for elements in set A
set_A = set(map(int, input().split()))

#cmd_len for no of operations performed.
cmd_len = int(input())
for i in range(cmd_len):
    # cmd for operations
    cmd = input().split()
    if cmd[0] == 'intersection_update':
        #ele for temp variable to store elements in particular operation
        ele = set(map(int, input().split()))
        set_A.intersection_update(ele)
    elif cmd[0] == 'update':
        ele = set(map(int, input().split()))
        set_A.update(ele)
    elif cmd[0] == 'symmetric_difference_update':
        ele = set(map(int, input().split()))
        set_A.symmetric_difference_update(ele)
    else:
        ele = set(map(int, input().split()))
        set_A.difference_update(ele)
print(sum(list(set_A)))