def simple(n):
    f = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            f += 1
    if f > 0:
        return True
    else:
        return False


k = int(input("Введите число "))
print([i for i in range(0, k)if simple(i)])
