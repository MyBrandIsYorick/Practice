from functools import reduce

l = input().split()
for i in range(0, len(l)):
    l[i] = float(l[i])
print(reduce(lambda x, y: x + y, l) / len(l))
