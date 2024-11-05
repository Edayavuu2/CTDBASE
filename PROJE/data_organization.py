# data_organization.py
import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)  # Eksik verileri temizle
    # Gereksiz sütunları kaldırma
    df = df[['column1', 'column2', 'column3']]  # Analizde kullanmak istediğiniz sütunları ekleyin
    return df

if __name__ == "__main__":
    organized_data = clean_data("ctdbase_data.csv")
    organized_data.to_csv("organized_data.csv", index=False)
    print("Veri temizlendi ve organize edildi.")
