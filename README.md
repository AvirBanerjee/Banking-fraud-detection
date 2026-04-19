#  Banking Fraud Detection System

A full-stack Banking Fraud Detection System that detects fraudulent transactions in real-time using Machine Learning, rule-based logic, and behavioral analysis.

---

##  Features

- Real-time fraud detection
- Machine Learning model (XGBoost)
- Rule-based + behavioral analysis
- Risk scoring system
- Explainable output (reasons for fraud)
- Alert system (Low / Medium / High)

---

##  Tech Stack

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

##  Dataset Setup

Dataset used:

 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Steps:

1. Download dataset from Kaggle
2. Extract the file
3. Copy `creditcard.csv`
4. Paste it inside:

Note:
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
pip install fastapi uvicorn pandas numpy scikit-learn xgboost joblib sqlalchemy 

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

