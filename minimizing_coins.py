n, x = [int(s) for s in input().split()]

coins = [int(s) for s in input().split()]

# O(nx) time complexity, O(x) space complexity solution
memo = []
i = 0
while i <= x:
    possible_sols = []
    for coin in coins:
        prev_ind = len(memo) - coin
        if i == coin:
            possible_sols.append(1)
        if prev_ind > 0 and memo[prev_ind] != -1:
            possible_sols.append(memo[prev_ind] + 1)
    if possible_sols:
        memo.append(min(possible_sols))
    else:
        memo.append(-1)
    
    i += 1
print(memo[-1])
