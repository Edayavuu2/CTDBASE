# interface.py
import requests
from tkinter import Tk, Label, Entry, Button

def send_request():
    user_input = {
        "feature1": float(entry_feature1.get()),
        "feature2": float(entry_feature2.get())
        # Diğer özellikleri ekleyin
    }
    response = requests.post("http://127.0.0.1:5000/predict", json=user_input)
    result = response.json().get("prediction", "Tahmin alınamadı.")
    label_result.config(text=f"Tahmin Sonucu: {result}")

app = Tk()
app.title("CTDBASE Makine Öğrenmesi Tahmin Uygulaması")

Label(app, text="Feature 1:").pack()
entry_feature1 = Entry(app)
entry_feature1.pack()

Label(app, text="Feature 2:").pack()
entry_feature2 = Entry(app)
entry_feature2.pack()

Button(app, text="Tahmin Et", command=send_request).pack()
label_result = Label(app, text="Tahmin Sonucu:")
label_result.pack()

app.mainloop()
