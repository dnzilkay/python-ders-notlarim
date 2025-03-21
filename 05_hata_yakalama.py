# Basit try-except kullanımı
try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 10 / sayi
    print(f"Sonuç: {sonuc}")
except ZeroDivisionError:
    print("0'a bölme hatası!")
except ValueError:
    print("Geçersiz giriş, lütfen sayı girin.")
else:
    print("Hata oluşmadı, işlemler başarılı.")
finally:
    print("Bu blok her zaman çalışır.")  # Bağlantı kapatma gibi işlemler için ideal

# Kendi hatamızı üretelim
def pozitif_sayi_kontrol(sayi):
    if sayi < 0:
        raise ValueError("Negatif sayı girdiniz!")
    return sayi

try:
    deger = int(input("Pozitif bir sayı girin: "))
    pozitif_sayi_kontrol(deger)
    print("Tebrikler, doğru giriş!")
except ValueError as e:
    print(f"Hata: {e}")
