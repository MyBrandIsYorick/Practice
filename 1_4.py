def main():
    chislo = int(input("Введите число от 10 до 20 - "))
    if chislo < 10:
        print("Число меньше требуемого диапазона")
        main()
    elif chislo > 20:
        print("Число больше требуемого значения")
        main()
    else:
        print("Спасибо")


main()
