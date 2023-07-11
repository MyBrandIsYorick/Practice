import csv


def searching():
    author = str(input("Введите автора, которого хотели бы найти - "))
    with open("books.csv", encoding="utf-8") as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if row["Автор"] == author:
                print(row)
                count += 1
    if count == 0:
        print("Книги данного автора не найдены")
    main()


def adding():
    count = int(input("Введите количество книг, которые вы хотите добавить - "))
    with open("books.csv", mode="a", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        while count > 0:
            print("Введите название книги, автора и год выпуска через запятую")
            s = str(input())
            l = s.split(',')
            file_writer.writerow([l[0], l[1], l[2]])
            count -= 1
    print("Книги были успешно добавлены")
    main()


def main():
    print("Что вы хотите?")
    print("Книги по автору - 1")
    print("Добавить книги - 2")
    choice = int(input("Выберите цифру - "))
    match choice:
        case 1:
            searching()
        case 2:
            adding()


main()
