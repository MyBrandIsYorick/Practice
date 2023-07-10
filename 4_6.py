def Caesar(st):
    di = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    sn = ""
    for i in range(len(st)):
        nind = (di.find(st[i]) + ke) % len(di)
        sn += di[nind]
    return sn


s = str(input("Введите строку "))
ke = int(input("Введите ключ "))
print(Caesar(s))
