s = list(str(input()))
while s.count(" "):
    s.remove(" ")
print({d: s.count(d) for d in s})
