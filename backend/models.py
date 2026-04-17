from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    amount = Column(Float)
    location = Column(String)
    device = Column(String)
    transaction_type = Column(String)
    is_international = Column(Boolean)

    risk_score = Column(Integer)
    decision = Column(String)
    status = Column(String)