# Sınıf (class) tanımı
class Araba:
    # Yapıcı metod (constructor)
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    # Metot tanımı
    def bilgileri_goster(self):
        print(f"{self.yil} model {self.marka} {self.model}")

    def calistir(self):
        print(f"{self.marka} {self.model} çalıştırıldı.")

# Nesne oluşturma
araba1 = Araba("Toyota", "Corolla", 2020)
araba2 = Araba("Ford", "Focus", 2018)

# Metotları kullanma
araba1.bilgileri_goster()
araba1.calistir()

araba2.bilgileri_goster()
araba2.calistir()
