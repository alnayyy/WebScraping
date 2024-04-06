# Import package requests, datetime, json, dan BeautifulSoup
import requests 
import datetime
import json
from bs4 import BeautifulSoup

# Request ke website
page = requests.get("https://www.republika.co.id/")
 
#  Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text,'html.parser')

scraping_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
news = obj.find_all('li', class_='list-group-item list-border conten1')
data_berita = []

print("\nScraping dilakukan pada:", scraping_time)

print('\nMenampilkan semua berita')
print('=====================================')
count = 0
for berita in news:
    judul = berita.find('h3').text.strip()
    date_div = berita.find('div', class_='date')
    kategori = date_div.find('span', class_='kanal-info').text.strip() 
    tanggal_publish = date_div.text.split('-')[-1].strip()
    
    print("Berita", count+1)
    print("Kategori:", kategori)
    print("Waktu Publikasi:", tanggal_publish)
    print("Judul Berita:", judul, "\n")
    count+=1
    
    # Membuat Dictionary untuk menyimpan data
    berita_dict = {
        'judul': judul,
        'kategori': kategori,
        'waktu_publish': tanggal_publish,
        'waktu_scraping': str(scraping_time)  
    }
    
    # Menambahkan dictionary berita ke list data_berita
    data_berita.append(berita_dict)
    
    with open('berita.json', 'w') as f:
        json.dump(data_berita, f, indent=4)