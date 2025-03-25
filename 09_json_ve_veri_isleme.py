import json

# Python sözlüğü
kullanici = {
    "ad": "Mehmet",
    "yas": 28,
    "diller": ["Python", "JavaScript"],
    "aktif": True
}

# Sözlüğü JSON formatında dosyaya yaz
with open("kullanici.json", "w", encoding="utf-8") as dosya:
    json.dump(kullanici, dosya, ensure_ascii=False, indent=4)

# JSON dosyasını tekrar Python sözlüğüne yükle
with open("kullanici.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)
    print("JSON'dan gelen veri:")
    print(veri)
