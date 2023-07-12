import requests
from bs4 import BeautifulSoup

while True:
    try:
        link = input("Ссылка на исполнителя на hitmos: ")
        response = requests.get(link)
        break
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidURL,
            requests.exceptions.InvalidSchema):
        print("Неверная ссылка! Попробуйте еще раз.")

# Парсинг HTML
soup = BeautifulSoup(response.text, "lxml")
artist_name = soup.find_all("li", class_="breadcrumb-item")
songs = soup.find_all("div", class_="track__title")

# Вывод песен
print(f"10 самых популярных треков исполнителя {artist_name[1].text.strip()}: ")
for i in range(10):
    print(f"{i+1}. - {songs[i].text.strip()}")
