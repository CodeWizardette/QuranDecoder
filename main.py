"""
بسم الله الرحمن الرحيم
"""
import matplotlib.pyplot as plt
from collections import Counter
import string

def ebcet_hesapla(kelime):
    ebcet_tablosu = {
        'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
        'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
        'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
        'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
    }
    
    ebcet_degeri = 0
    for harf in kelime:
        ebcet_degeri += ebcet_tablosu.get(harf, 0)
    
    return ebcet_degeri

def metin_temizle(metin):
    temiz_metin = metin.replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("-", "").replace("_", "").replace("/", "").replace("\\", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("+", "").replace("=", "").replace("|", "").replace("~", "").replace("`", "").replace("<", "").replace(">", "")
    temiz_metin = temiz_metin.lower()
    return temiz_metin

def kelime_frekansi(metin):
    kelimeler = metin.split()
    frekanslar=defaultdict(int)
    for kelime in kelimeler
        frekanslar[kelime] +=1
    return frekanslar

def kelime_uzunlugu_histogrami(metin):
    kelimeler = metin.split()
    uzunluklar = [len(kelime) for kelime in kelimeler]
    plt.hist(uzunluklar, bins=range(min(uzunluklar), max(uzunluklar) + 2, 1), edgecolor='black')
    plt.xlabel('Kelime Uzunluğu')
    plt.ylabel('Frekans')
    plt.title('Kelime Uzunluğu Histogramı')
    plt.show()

def kelime_freksansi_grafik(metin, en_cok=10):
    frekanslar = kelime_frekansi(metin)
    en_cok_kelimeler = frekanslar.most_common(en_cok)
    kelimeler, frekanslar = zip(*en_cok_kelimeler)
    plt.bar(kelimeler, frekanslar)
    plt.xlabel('Kelime')
    plt.ylabel('Frekans')
    plt.title(f'En Sık {en_cok} Kelime')
    plt.xticks(rotation=45)
    plt.show()
    
    
    
with open("kuran.txt", "r", encoding="utf-8") as file:
    kuran_metni = file.read()7

kuran_metni = """
Buraya Kur'an metnini ekleyin.
"""
temiz_metin = metin_temizle(kuran_metni)

# Stop kelimeleri çıkar
nltk.download('stopwords')
stop_kelimeler = set(stopwords.words('turkish'))
kelimeler = temiz_metin.split()
kelimeler_filtrli = [kelime for kelime in kelimeler if kelime not in stop_kelimeler]

kelime_uzunlugu_histogrami(kelimeler_filtrli)
frekanslar = kelime_frekansi(kelimeler_filtrli)
kelime_freksansi_grafik(frekanslar)

# Bigram frekans analizi
bigramler = ngrams(kelimeler_filtrli, 2)
bigram_frekanslar = defaultdict(int)
for bigram in bigramler:
    bigram_frekanslar[bigram] += 1

kelime_freksansi_grafik(bigram_frekanslar, en_cok=10)

temiz_metin = metin_temizle(kuran_metni)
kelime_uzunlugu_histogrami(temiz_metin)
kelime_freksansi_grafik(temiz_metin)

# Grafik gösterme yerine kaydetme
plt.savefig("kelime_uzunlugu_histogrami.png")
plt
