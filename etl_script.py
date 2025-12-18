import requests
import pandas as pd

url = "https://api.frankfurter.app/latest?from=USD&to=TRY,EUR,GBP"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    # Kurları DataFrame'e çeviriyoruz
    df = pd.DataFrame(
        list(data["rates"].items()),
        columns=['doviz', 'kur']
    )
    
    # 'tarih' ve 'kaynak' sütunları ekleniyor
    df['tarih'] = data.get("date", "")
    df['kaynak'] = data.get("base", "")

    # SQLAlchemy ile PostgreSQL'e bağlantı ve veri yükleme
    from sqlalchemy import create_engine

    db_url = 'postgresql://deniz:sifre123@localhost:5432/postgres'
    engine = create_engine(db_url)

    df.to_sql('doviz_kurlari', engine, if_exists='replace', index=False)

    print("Veri başarıyla veritabanına yüklendi!")
    
    print(df)
except Exception as e:
    print(f"Hata oluştu: {e}")
