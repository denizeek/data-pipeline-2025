from typing import List, Dict

# Sahte borsa verisi oluşturuluyor
borsa_verisi: List[Dict[str, any]] = [
    {"id": 1, "isim": "HisseA", "fiyat": 25.0},
    {"id": 2, "isim": "HisseB", "fiyat": 45.5},
    {"id": 3, "isim": "HisseC", "fiyat": 32.2},
    {"id": 4, "isim": "HisseD", "fiyat": 18.7},
    {"id": 5, "isim": "HisseE", "fiyat": 50.0},
    {"id": 6, "isim": "HisseF", "fiyat": 29.9},
    {"id": 7, "isim": "HisseG", "fiyat": 35.1},
    {"id": 8, "isim": "HisseH", "fiyat": 41.3},
    {"id": 9, "isim": "HisseI", "fiyat": 27.5},
    {"id": 10, "isim": "HisseJ", "fiyat": 60.4},
]

def filtrele_ve_yazdir(veriler: List[Dict[str, any]]) -> None:
    filtrelenmis: List[Dict[str, any]] = [v for v in veriler if v["fiyat"] > 30]
    for veri in filtrelenmis:
        print(veri)

filtrele_ve_yazdir(borsa_verisi)
