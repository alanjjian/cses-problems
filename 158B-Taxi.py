import sys
from collections import defaultdict
from math import ceil
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


num_grp = inp()
grp_lst = list(invr())
size_ct = defaultdict(int)

for grp_size in grp_lst:
    size_ct[grp_size] += 1

num_taxi = size_ct[4] # best use of taxis

# 2nd best: every group of 3 gets a group of 1
size_ct[1] = max(size_ct[1] - size_ct[3], 0)
num_taxi += size_ct[3]

# 3rd best: every group of 2 gets another group of 2 or two groups of 1
if size_ct[2] % 2 == 0:
    num_taxi += size_ct[2] / 2
else:
    num_taxi += size_ct[2] // 2 + 1
    size_ct[1] = max(size_ct[1] - 2, 0)

#4th best: rest of the groups of 1 get shoveled in
num_taxi += ceil(size_ct[1] / 4)

print(int(num_taxi))
