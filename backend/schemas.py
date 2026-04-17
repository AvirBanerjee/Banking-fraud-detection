from pydantic import BaseModel

class UserHistory(BaseModel):
    avg_amount: float
    usual_location: str
    usual_time: str

class TransactionSchema(BaseModel):
    user_id: str
    amount: float
    location: str
    device: str
    time: str
    transaction_type: str
    is_international: bool
    user_history: UserHistory