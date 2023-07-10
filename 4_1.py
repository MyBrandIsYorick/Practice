s = str(input())
ns = list(int(d) for d in list(s))
ns.sort(reverse=True)
ma = ""
for i in range(len(ns)):
    ma += str(ns[i])
print(ma)
