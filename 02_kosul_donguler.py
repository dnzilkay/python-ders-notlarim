# KOŞULLAR (if-elif-else)
print("Koşul ifadeleriyle karar yapıları:")

yas = int(input("Yaşınızı girin: "))

if yas < 18:
    print("Reşit değilsiniz.")
elif 18 <= yas < 65:
    print("Çalışma çağındasınız.")
else:
    print("Emeklilik yaşına gelmişsiniz.")

# TEK VE ÇİFT SAYI KONTROLÜ
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır.")
else:
    print(f"{sayi} tek bir sayıdır.")

# DÖNGÜLER (for, while)
print("\nFor ve While döngüleri:")

# 1'den 10'a kadar olan sayıları yazdıran for döngüsü
for i in range(1, 11):
    print(i, end=" ")

print("\nWhile döngüsü ile sayaç:")
sayac = 5
while sayac > 0:
    print(f"Kalan: {sayac}")
    sayac -= 1

print("Döngü tamamlandı!")

# BREAK ve CONTINUE kullanımı
print("\nBreak ve Continue kullanımı:")

for i in range(1, 6):
    if i == 3:
        print("3 atlandı (continue kullanıldı).")
        continue
    if i == 5:
        print("5'te döngü sonlandırıldı (break kullanıldı).")
        break
    print(i)

print("Koşullar ve döngüler konusu tamamlandı!")
