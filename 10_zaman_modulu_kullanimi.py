import time
from datetime import datetime

# Şu anki tarih ve saat
simdi = datetime.now()
print("Şu an:", simdi.strftime("%Y-%m-%d %H:%M:%S"))

# Uyutma örneği
print("3 saniye bekleniyor...")
time.sleep(3)
print("Devam edildi!")

# Zaman karşılaştırması
baslangic = time.time()

# Örnek işlem (liste oluşturma)
liste = [i ** 2 for i in range(1000000)]

bitis = time.time()
print(f"İşlem süresi: {bitis - baslangic:.2f} saniye")
