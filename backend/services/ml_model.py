import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "ml", "model.pkl")

model = joblib.load(model_path)


def predict(transaction):
    hour = int(transaction.time.split(":")[0])

    features = np.array([
        transaction.amount,
        hour,
        1 if transaction.is_international else 0
    ]).reshape(1, -1)

    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0][1]  # 🔥 important

    return int(pred), float(proba)