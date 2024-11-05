# app.py
from flask import Flask, request, jsonify
import pandas as pd
from model_training import train_model

app = Flask(__name__)

# Modeli eğitme ve yükleme
model = train_model("organized_data.csv")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])  # JSON'u DataFrame'e dönüştür
    prediction = model.predict(input_data)[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
