import collections

n = int(input())
lst = [int(char) for char in input().split()]

tree = collections.defaultdict(list)

employee = 0
while employee < len(lst):
    curr_boss = lst[employee]
    tree[curr_boss].append(employee + 2)
    employee += 1


memo = [-1 for i in range(n + 1)]

# broot force :3

"""def get_num_subordinates(n, memo):
    if n in memo:
        return memo[n]
    num_subords = len(tree[n])
    for subord in tree[n]:
        if memo[subord] == -1: 
            memo[subord] = get_num_subordinates(subord, memo)
        num_subords += memo[subord]
    memo[n] = num_subords
    return num_subords

get_num_subordinates(1, memo)
print(" ".join([str(i) for i in memo[1:]]))"""
