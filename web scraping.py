import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

names_items = []
prixes_items = []
disponbilites_items = []
refrences_items = []

for i in range(1, 13):
    url = f"https://www.mytek.tn/informatique/ordinateur-de-bureau/ordinateur-gamer.html?p={i}"

    r = requests.get(url)
    src = r.content

    soup = BeautifulSoup(src, 'lxml')

    name_items = soup.find_all("strong", {"class": "product name product-item-name"})
    prixe_items = soup.find_all("span", {"class": "price"})
    disponbilite_items = soup.find_all("div", {"class": "card-body"})
    refrence_items = soup.find_all("div", {"class": "skuDesktop"})

    for i in range(len(name_items)):
        names_items.append(name_items[i].text.strip() if i < len(name_items) else 'N/A')
        prixes_items.append(prixe_items[i].text.strip() if i < len(prixe_items) else 'N/A')
        disponbilites_items.append(disponbilite_items[i].text.strip() if i < len(disponbilite_items) else 'N/A')
        refrences_items.append(refrence_items[i].text.strip() if i < len(refrence_items) else 'N/A')

file_list = [names_items, prixes_items, disponbilites_items, refrences_items]
exported = zip_longest(*file_list, fillvalue='N/A')

csv_file_path = "C:\\Users\\mouha\\PycharmProjects\\pythonProject2\\mytek_products1.csv"

with open(csv_file_path, "w", newline='', encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["names_items", "prixes_items", "disponbilites_items", "refrences_items"])
    wr.writerows(exported)

print("Data has been written to the CSV file.")
