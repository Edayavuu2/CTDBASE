# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(data_path):
    df = pd.read_csv(data_path)
    X = df.drop('target_column', axis=1)  # Hedef sütunu hariç tüm sütunlar
    y = df['target_column']  # Hedef sütun

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model doğruluk oranı: {accuracy}")

    return model

if __name__ == "__main__":
    model = train_model("organized_data.csv")

