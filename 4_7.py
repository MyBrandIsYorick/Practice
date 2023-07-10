import itertools

li = input("Введите список чисел ").split()

for i in itertools.permutations(li):
    print(*i)
