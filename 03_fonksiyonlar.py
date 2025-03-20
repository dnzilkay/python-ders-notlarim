# Fonksiyonlar (Functions) - Python'da Fonksiyon Kullanımı

# 1. Basit Fonksiyon Tanımlama
def selamla():
    """Bu fonksiyon ekrana bir selamlama mesajı yazar."""
    print("Merhaba, Python dünyasına hoş geldiniz!")

selamla()  # Fonksiyonu çağırma

# 2. Parametre Alan Fonksiyon
def topla(a, b):
    """İki sayının toplamını döndürür."""
    return a + b

sonuc = topla(5, 10)
print("Toplam:", sonuc)

# 3. Varsayılan Parametre Kullanan Fonksiyon
def merhaba(isim="Ziyaretçi"):
    print(f"Merhaba, {isim}!")

merhaba()  # Varsayılan değer kullanılır
merhaba("Ahmet")

# 4. *args ile Değişken Sayıda Argüman

def ortalama(*sayilar):
    """Girilen tüm sayıları alır ve ortalamasını döndürür."""
    return sum(sayilar) / len(sayilar)

print("Ortalama:", ortalama(10, 20, 30, 40))

# 5. **kwargs ile Anahtar Kelime Argümanları

def kisi_bilgileri(**bilgiler):
    """Kişi bilgilerini yazdırır."""
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

kisi_bilgileri(isim="Mehmet", yas=25, sehir="Ankara")

# 6. Lambda Fonksiyonları
kare_al = lambda x: x ** 2
print("5'in karesi:", kare_al(5))

# 7. map ve filter Kullanımı
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print("Kareler:", kareler)

ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift Sayılar:", ciftler)

# 8. Özyinelemeli (Recursive) Fonksiyon

def faktoriyel(n):
    """n! hesaplayan özyinelemeli fonksiyon"""
    if n == 1:
        return 1
    return n * faktoriyel(n - 1)

print("5!:", faktoriyel(5))

# 9. Hata Yönetimi ile Fonksiyon

def bolme(a, b):
    """İki sayıyı böler, sıfıra bölme hatasını yakalar."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Hata: Sıfıra bölme yapılamaz!"

print(bolme(10, 2))
print(bolme(10, 0))
