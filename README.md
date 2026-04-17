# 🏦 Banking Fraud Detection System

A full-stack Banking Fraud Detection System that detects fraudulent transactions in real-time using Machine Learning, rule-based logic, and behavioral analysis.

---

## 🚀 Features

- Real-time fraud detection
- Machine Learning model (XGBoost)
- Rule-based + behavioral analysis
- Risk scoring system
- Explainable output (reasons for fraud)
- Alert system (Low / Medium / High)

---

## 🧠 Tech Stack

### Backend
- FastAPI
- Python
- XGBoost
- Pandas, NumPy

### Frontend
- React (Vite)
- Tailwind CSS
- Axios
- React Hot Toast

---

## 📊 Dataset Setup

Dataset used:

👉 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Steps:

1. Download dataset from Kaggle
2. Extract the file
3. Copy `creditcard.csv`
4. Paste it inside:
backend/ml/creditcard.csv


⚠️ Note:
- Dataset is NOT included in this repo due to GitHub size limits
- You must download it manually

---

## ⚙️ Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pandas numpy scikit-learn xgboost joblib

# Train ML model
python train_model.py

# Run backend server
uvicorn main:app --reload
```
Backend URLs:
API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs

cd frontend

# Install dependencies
npm install

# Start frontend
npm run dev
Frontend URL:

http://localhost:5173

Project Flow
User enters transaction details in frontend
Data is sent to FastAPI backend
ML model predicts fraud probability
Rule-based + behavioral analysis applied
Risk score is generated
Decision (Approve / Block / Investigate) is returned
Result is displayed on UI

Future Improvements
Admin dashboard
Fraud analytics charts
User authentication (RBAC)
Real-time streaming (Kafka)

This README Gives You

✔ Clean structure  
✔ Dataset path clarity  
✔ Setup steps (backend + frontend)  
✔ API usage  
✔ Professional impression  


