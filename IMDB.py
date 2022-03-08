from builtins import Exception

import requests
import json
import time
import re
import textwrap

apim = "YOUR API KEY"
siteForApi = "https://imdb-api.com/"

class Film:
    def __init__(self):
        self.dongu = True
    def program(self):
        secim = self.menu()

        if secim == "1":
            self.best250()
        if secim == "2":
            self.popularMovies()
        if secim == "3":
            self.gosterimde()
        if secim == "4":
            self.yakindaSinemalarda()
        if secim == "5":
            self.filmAra()
        if secim == "6":
            self.cikis()
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim):
                raise Exception("Lütfen 1-6 arasında seçim yapınız!!!")
        while True:
            try:
                secim = input("""
Merhaba, IMDB Progragramına Hoşgeldiniz
Lütfen yapmak istedğiniz işlemi seçiniz
1)En iyi 250 Film
2)En Popüler Filmler
3)Sinemalardaki Filmler
4)Yakında Sinemalarda
5)Film Ara
6)Çıkış\n """)
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secim

    def best250(self):
        print("En iyi 250 Film Listesine Ulaşılıyor... \n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/Top250Movies/{}".format(apim))
        sonuc = url.json()
        for i in sonuc["items"]:
            print("Film Adı = ",i["fullTitle"],"IMDB Puanı = ",i["imDbRating"])
        self.menuDon()

    def popularMovies(self):
        print("En Popüler Filmler Listesine Ulaşılıyor... \n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/MostPopularMovies/{}".format(apim))
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()
    def gosterimde(self):
        print("Gösterimde Olan Filmler Listesine Ulaşılıyor... \n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/InTheaters/{}".format(apim))
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()
    def yakindaSinemalarda(self):
        print("Yakında Sinemlarda Olacak Filmler Listesine Ulaşılıyor... \n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/ComingSoon/{}".format(apim))
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menuDon()
    def filmAra(self):
        print("Film Arama Menüsüne Ulaşılıyor \n\n")
        time.sleep(2)
        film = input("Lütfen film adını giriniz = ")

        url = requests.get("https://imdb-api.com/en/API/Top250Movies/{}".format(apim))
        sonuc = url.json()
        id =[]
        name = []
        for i in sonuc["items"]:
            id.append(i["id"])
        for i in sonuc["items"]:
            name.append(i["title"])
        zipped = zip(name,id)
        veri = dict(zipped)
        key = veri.get(film)

        url2 = requests.get("https://imdb-api.com/tr/API/Wikipedia/{}/{}".format(apim,key))
        sonuc2 = url2.json()
        print(textwrap.fill(sonuc2["plotShort"]["plainText"]),130)
        self.menuDon()

    def cikis(self):
        print("Çıkılıyor")
        time.sleep(2)
        self.dongu=False
        exit()

    def menuDon(self):
        while True:
            x = input("""
Ana Menüye Dönmek İçin 7'ye basınız
Çıkmak İçin Lütfen 6'ya basınız
""")
            if x == "7":
                print("Ana Menüye Dönülüyor")
                time.sleep(2)
                self.program()
                break
            if x == "6":
                self.cikis()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız")

Sistem = Film()
while Sistem.dongu:
    Sistem.program()

