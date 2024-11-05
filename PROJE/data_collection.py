# data_collection.py
import requests
import pandas as pd

def fetch_data():
    # CTDBASE API URL'sini ekleyin
    url = 'https://ctdbase.org/api/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # JSON formatında veriyi alın
        return pd.DataFrame(data)
    else:
        print("Veri çekme hatası:", response.status_code)
        return None

if __name__ == "__main__":
    data = fetch_data()
    if data is not None:
        data.to_csv("ctdbase_data.csv", index=False)
        print("Veri başarıyla indirildi ve kaydedildi.")
