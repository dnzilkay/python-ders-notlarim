# Ana sınıf
class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        print(f"{self.isim} bir ses çıkarıyor.")

# Alt sınıf – Köpek
class Kopek(Hayvan):
    def ses_cikar(self):
        print(f"{self.isim} havlıyor!")

# Alt sınıf – Kedi
class Kedi(Hayvan):
    def ses_cikar(self):
        print(f"{self.isim} miyavlıyor!")

# Nesneler oluştur
kopek1 = Kopek("Karabas")
kedi1 = Kedi("Minnak")

# Metotları çağır
kopek1.ses_cikar()
kedi1.ses_cikar()
