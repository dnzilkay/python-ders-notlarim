# 1. Dosya yazma (write)
with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Bu ilk satırdır.\n")
    dosya.write("Python dosya işlemleri çok kolay!\n")

# 2. Dosya okuma (read)
with open("notlar.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("Dosya İçeriği:")
    print(icerik)

# 3. Dosyaya ekleme (append)
with open("notlar.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Bu satır eklenmiştir.\n")

# 4. Satır satır okuma
with open("notlar.txt", "r", encoding="utf-8") as dosya:
    print("Satır Satır Okuma:")
    for satir in dosya:
        print(satir.strip())
