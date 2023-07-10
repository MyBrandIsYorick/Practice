from itertools import combinations
from functools import reduce


def Summ(li):
    return reduce(lambda x, y: x + y, li)


int_list = []
for element in input("Введите список ").split():
    int_list.append(int(element))
s = int(input("Введите число-сумму "))

for j in range(1, 5):
    for i in combinations(int_list, j):
        if Summ(i) == s:
            print(*i)
