import csv


def searching():
    start_year, end_year = map(int, input("Введите начальную и конечную дату - ").split())
    with open("books.csv", encoding="utf-8") as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if start_year <= int(row["Год выпуска"]) <= end_year:
                print(row)
                count += 1
    if count == 0:
        print("Книги в данном временном отрезке не найдены")


searching()
