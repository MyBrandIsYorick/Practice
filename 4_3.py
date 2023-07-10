def simple(n):
    k = 0
    for p in range(2, n // 2 + 1):
        if n % p == 0:
            k += 1
    if k > 0:
        return False
    else:
        return True


a, b = map(int, input("Введите диапазон чисел").split())

for i in range(a, b+1):
    if simple(i):
        print(i)
