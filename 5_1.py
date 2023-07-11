import csv

with open("books.csv", mode="w", encoding="utf-8")as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(["Книга", "Автор", "Год выпуска"])
    file_writer.writerow(["Страж", "Алексей Пехов", "2010"])
    file_writer.writerow(["Красное на красном", "Вера Камша", "2004"])
    file_writer.writerow(["Человек, который принял жену за шляпу", "Оливер Сакс", "2021"])
    file_writer.writerow(["Убийственная шутка", "Криста Фауст", "2019"])
