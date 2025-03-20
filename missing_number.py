n = int(input())
nums = [int(s) for s in input().split()]

print(int((n * (n + 1)) / 2  - sum(nums)))