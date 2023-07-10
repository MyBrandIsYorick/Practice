d1 = int(input("Число 1 - "))
d2 = int(input("Число 2 - "))
d3 = int(input("Число 3 - "))
ma = max(d1, d2, d3)
mi = min(d1, d2, d3)
su = d1 + d2 + d3
midl = su - ma - mi
print(f"Число {ma} является наибольшим")
print(ma)
print(midl)
print(mi)
