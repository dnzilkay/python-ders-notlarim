import os

# Geçerli çalışma dizinini al
print("Geçerli dizin:", os.getcwd())

# Yeni klasör oluştur
klasor_adi = "deneme_klasoru"
if not os.path.exists(klasor_adi):
    os.mkdir(klasor_adi)
    print(f"'{klasor_adi}' klasörü oluşturuldu.")
else:
    print(f"'{klasor_adi}' zaten var.")

# Klasör içeriğini listele
print("Klasör içeriği:", os.listdir("."))

# Dosya oluştur
dosya_yolu = os.path.join(klasor_adi, "bilgi.txt")
with open(dosya_yolu, "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba Python")

print(f"{dosya_yolu} dosyası oluşturuldu ve yazıldı.")
