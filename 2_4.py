from math import sqrt

a, b, c = map(float, input().split())
dif = b ** 2 - 4 * a * c
if dif < 0:
    print("Корней нет")
elif dif == 0:
    x = -b / (2 * a)
    print(f"Один корень - {x}")
else:
    x1 = (-b + sqrt(dif)) / (2 * a)
    x2 = (-b - sqrt(dif)) / (2 * a)
    print(f"x1 = {x1} x2 = {x2}")
