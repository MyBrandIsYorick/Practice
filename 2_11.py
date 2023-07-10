a, b = map(int, input("Введите два числа").split())
s = 0
for i in range(a, b + 1):
    s += i

print(s)
