import sys
import requests
from bs4 import BeautifulSoup
import db_connect
from pymongo.errors import DuplicateKeyError


current_path = sys.path[0]
print(f"Current working directory: {current_path}")


url = 'https://en.wikipedia.org/wiki/List_of_most_populous_municipalities_in_Belgium'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# HTML içindeki ilgili etiketleri seç
rows = soup.select('table.wikitable tr')[1:]  # İlk satır başlıkları içerdiği için 1'den başlıyoruz.

city_list = []

# Her satırdaki belediye isimlerini ve nüfus bilgilerini çek
for row in rows:
    columns = row.select('td')
    
    # Belediye bilgisi içeren satırları kontrol et
    if columns:
        city = columns[1].select_one('a').text
        population = columns[6].text.strip().replace(',', '')  # Virgülü temizle ve boşlukları kaldır
        population = int(population) if population.isdigit() else None  # Nüfusu sayıya çevir (sayısal değilse None yap)

        # Elde edilen verileri bir sözlük içinde tut
        city_data = {'city': city, 'population': population}
        city_list.append(city_data)

# MongoDB koleksiyonuna eklenmeden önce ülke bilgisini ekleyin
formatted_data = {'Belgium': city_list }
#print(formatted_data)

db_connection = db_connect.get_db_connection()
# Önce koleksiyondan bu ülkenin var olup olmadığını kontrol edelim
existing_data = db_connection.find_one({'Belgium': {'$exists': True}})

if existing_data:
    # Eğer ülke zaten varsa, güncelleme veya eklemeye karar verebilirsiniz
    print(f"Data for {formatted_data.keys()} already exists in the database.")
else:
    try:
        # Veritabanına ekleme işlemi
        db_connection.insert_one(formatted_data)
        print(f"Inserted data for {formatted_data.keys()} into the database.")
    except DuplicateKeyError:
        # Eğer aynı veri zaten varsa (anahtar çakışması), hatayı görmezden gel
        print(f"Data for {formatted_data.keys()} already exists in the database.")

