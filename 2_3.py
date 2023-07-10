def Armstrong(s):
    s1 = str(s)
    s2 = 0
    st = len(s1)
    for i in range(len(s1)):
        s2 += int(s1[i]) ** st
    if s2 == s:
        return True
    else:
        return False


chislo = int(input("Введите число - "))
if Armstrong(chislo):
    print(f"Число {chislo} число Армстронга")
else:
    print(f"Число {chislo} не является числом Армстронга")
