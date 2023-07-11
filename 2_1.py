from random import randint

mas = ["red", "green", "purple", "royal blue", "yellow"]
robot_color = str(mas[randint(0, 4)])
print("Я загадал цвет, напишите свой(из вариантов ниже) и если угадаете, то победите")
print("В противном случае я дам вам подсказку и ещё один шанс")


def main():
    for i in range(0, 5):
        print(mas[i])
    choice = str(input("Ваш выбор - "))
    if choice == robot_color:
        print("Вы угадали!!!")
    else:
        match robot_color:
            case "red":
                c = randint(0, 1)
                if c == 0:
                    print("Подсказка - этот цвет находится в трёх первых цветах радуги")
                else:
                    print("Подсказка - такого же цвета бывает кровь")
                main()
            case "green":
                print("Подсказка - в русском слове этого цвета есть буква ё")
                main()
            case "yellow":
                c = randint(0, 1)
                if c == 0:
                    print("Подсказка - этот цвет находится в трёх первых цветах радуги")
                    main()
                else:
                    print("Подсказка - в русском слове этого цвета есть буква ё")
                    main()
            case "purple":
                print("Hint - darker than pink")
                main()
            case "royal blue":
                print("Подсказка - такого же цвета бывает кровь")
                main()


main()
