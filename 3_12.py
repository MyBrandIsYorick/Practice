d = {i: i ** 3 for i in range(1, 10)}
print(dict(filter(lambda item: item[0] % 2 == 0, d.items())))
