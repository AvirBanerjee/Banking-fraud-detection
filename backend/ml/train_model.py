import pandas as pd
import os
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "creditcard.csv")

df = pd.read_csv(file_path)

print(" Dataset Loaded")


df["hour"] = (df["Time"] // 3600) % 24

df["is_international"] = (df["Amount"] > 3000).astype(int)

X = df[["Amount", "hour", "is_international"]]
y = df["Class"]

print("✅ Features Prepared:", X.columns.tolist())



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("✅ Data Split Done")

scale_pos_weight = len(y_train[y_train == 0]) / len(y_train[y_train == 1])


model = XGBClassifier(
    n_estimators=50,
    max_depth=6,
    learning_rate=0.1,
    objective="binary:logistic",
    eval_metric="logloss",
    scale_pos_weight=scale_pos_weight,
    use_label_encoder=False
)


print("\n Training Started...\n")

model.fit(
    X_train,
    y_train,
    eval_set=[(X_train, y_train), (X_test, y_test)],
    verbose=True
)

print("\n✅ Training Completed")


y_pred = model.predict(X_test)

print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))


model_path = os.path.join(BASE_DIR, "model.pkl")
joblib.dump(model, model_path)

print(f"\n Model saved at: {model_path}")