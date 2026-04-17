from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import TransactionSchema
from services import ml_model, rules_engine, behavioral, risk_scoring, decision_engine, xai

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/predict")
def predict_transaction(tx: TransactionSchema, db: Session = Depends(get_db)):

    # ML
    ml_pred, ml_proba = ml_model.predict(tx)

    # Rule & behavior
    rule_score = rules_engine.check(tx)
    behavior_score = behavioral.analyze(tx)

    # Risk score
    risk_score = risk_scoring.combine(ml_proba, rule_score, behavior_score)

    # Decision
    decision, status = decision_engine.decide(risk_score)

    # XAI
    reasons = xai.generate(
        tx,
        ml_proba,
        rule_score,
        behavior_score,
        risk_score
    )

    return {
        "risk_score": risk_score,
        "status": status,
        "decision": decision,
        "confidence": f"{ml_proba * 100:.2f}%",
        "reasons": reasons,
        "alert_level": "High" if risk_score > 70 else "Medium" if risk_score > 30 else "Low"
    }