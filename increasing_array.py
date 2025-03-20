leng = int(input())
lst = [int(num) for num in input().split()]
moves = 0
i = 1
while i < leng:
    if lst[i] < lst[i - 1]:
        moves += lst[i - 1] - lst[i]
        lst[i] = lst[i - 1]
    i += 1
print(moves)