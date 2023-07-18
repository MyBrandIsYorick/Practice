from functools import reduce

l = input().split()
a=[]
for i in range(0, len(l)):
   a.append(float(l[i]))
print(reduce(lambda x, y: x + y, a)/ len(l))
