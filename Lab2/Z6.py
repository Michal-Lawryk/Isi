import csv

import requests
from bs4 import BeautifulSoup


class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name.replace(",", "")
        self.price = price.replace("\xa0", ".").replace(".zł", "")
        self.price_for_m2 = price_for_m2


URL = (
    "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType"
    "=listing")
headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

offers = soup.find_all("article")

headers_name = []
for offer in offers:
    text = offer.find(class_="css-115o4jq ev8qziy4")
    text = text.text
    headers_name.append(text)

prices = []
for offer in offers:
    text = offer.find(class_="ev8qziy1 css-2ih7x0 e1a3ad6s0")
    text = text.text
    prices.append(text)

prices_for_m2 = []
for offer in offers:
    text = offer.find(class_="css-uki0wd e12r8p6s1")
    text = text.text
    text = text.replace(" ", "").replace(" ", ".")

    try:
        text = text[text.index('kwadratowy'):text.index('.zł')]
        text = text.replace("kwadratowy", "")
    except:
        text = "Zapytaj o cenę"

    if text[0] == '8' or text[0] == '9':
        text = text[0] + '.' + text[1:]
    prices_for_m2.append(text)

rows = []
homesDict = {}
for i in range(len(headers_name)):
    homesDict[i] = Home(headers_name[i], prices[i], prices_for_m2[i])
    rows.append({"Naglowek": homesDict[i].header_name, "Cena calkowita (zl)": homesDict[i].price, "Cena za metr (zl/m2)": homesDict[i].price_for_m2})


fields = ["Naglowek", "Cena calkowita (zl)", "Cena za metr (zl/m2)"]
with open('oferty.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

file.close()
