from functools import reduce

n = int(input())
fib = lambda k: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(k - 2), [0, 1])

print(*fib(n))
