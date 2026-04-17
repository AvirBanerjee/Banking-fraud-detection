def generate(tx, ml_proba, rule_score, behavior_score, final_score):

    reasons = []

    
    if ml_proba > 0.7:
        reasons.append("High fraud probability from ML model")

    
    if tx.amount > 50000:
        reasons.append("High transaction amount")

    if tx.is_international:
        reasons.append("International transaction")

    
    if tx.location != tx.user_history.usual_location:
        reasons.append("Location anomaly")

    if tx.amount > tx.user_history.avg_amount * 5:
        reasons.append("Behavioral deviation")

   
    if final_score < 30:
        reasons = []  

    return reasons