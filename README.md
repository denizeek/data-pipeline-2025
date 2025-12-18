# 🚀 Döviz Kuru ETL Pipeline (Python & PostgreSQL & Docker)

Bu proje, gerçek zamanlı döviz verilerini bir API'den çeken (**Extract**), veriyi analiz edilebilir formata dönüştüren (**Transform**) ve Dockerize edilmiş bir PostgreSQL veritabanında saklayan (**Load**) uçtan uca bir veri mühendisliği projesidir.

## 🏗 Mimari

Proje **Microservice** mimarisine uygun olarak tasarlanmıştır ve iki ana bileşenden oluşur:
1.  **ETL Servisi:** Python (Pandas, SQLAlchemy) tabanlı veri işleme motoru.
2.  **Veritabanı:** Verilerin kalıcı olarak saklandığı PostgreSQL servisi.

Her iki servis de **Docker Container** içinde izole edilmiş ve özel bir **Docker Network** üzerinden haberleşmektedir.

## 🛠 Kullanılan Teknolojiler

*   **Dil:** Python 3.11
*   **Veritabanı:** PostgreSQL
*   **Konteynerizasyon:** Docker
*   **Kütüphaneler:** Pandas, SQLAlchemy, Psycopg2, Requests
*   **Versiyon Kontrol:** Git & GitHub

## ⚙️ Kurulum ve Çalıştırma

Bu projeyi bilgisayarınızda çalıştırmak için sadece **Docker**'ın kurulu olması yeterlidir. Python veya SQL kurmanıza gerek yoktur.

### 1. Projeyi Klonlayın
```bash
git clone https://github.com/denizeek/data-pipeline-2025.git
cd data-pipeline-2025