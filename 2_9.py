s = str(input())
d = list(s)

for i in range(0, len(d)):
    d[i] = int(d[i])

print(f"Индекс с начала = {d.index(max(d))}")
print(f"Индекс с конца = {len(d) - d.index(max(d)) - 1}")
