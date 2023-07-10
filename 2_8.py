n = int(input())

for i in range(0, round(n ** (1 / 2)) + 2):
    if i ** 2 > n:
        print(f"Нужное число = {i}")
        break
