from fastapi import FastAPI
from database import engine, Base
from routes.transaction import router as transaction_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction_router)

@app.get("/")
def root():
    return {"message": "Fraud Detection API Running"}