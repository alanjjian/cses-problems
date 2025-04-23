import collections

n = int(input())
lst = [int(char) for char in input().split()]

tree = collections.defaultdict(list)

employee = 0
while employee < len(lst):
    curr_boss = lst[employee]
    tree[curr_boss].append(employee + 2)
    employee += 1

trav = collections.deque()
trav.append(1)

trav2 = collections.deque()
trav2.append(1)

while True:
    if len(trav) == 0:
        break
    curr_employee = trav.pop()
    for subord in tree[curr_employee]:
        trav.appendleft(subord)
        trav2.appendleft(subord)

memo = [0 for i in range(n + 1)]
while True:
    if len(trav2) == 0:
        break
    curr_employee = trav2.popleft()
    memo[curr_employee] = len(tree[curr_employee])
    for subord in tree[curr_employee]:
        memo[curr_employee] += memo[subord]

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
"""
print(" ".join([str(i) for i in memo[1:]]))
