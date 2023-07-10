import sys


def inp():
    ch = int(input("Введите число - "))
    if ch < 0:
        return ch
    else:
        sys.exit()


s = 0
while True:
    s += inp()
    print(f"Current sum = {s}")
