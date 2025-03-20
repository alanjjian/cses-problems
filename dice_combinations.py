from collections import deque
n = int(input())

if n <= 6:
    print(2 ** (n - 1))
else:
    fib_6 = deque([2 ** i for i in range(6)])

    i = 7
    while i < n:
        new_fib_num = sum(fib_6)
        fib_6.popleft()
        fib_6.append(new_fib_num)
        i += 1
    print(sum(fib_6) % (10 ** 9 + 7))


