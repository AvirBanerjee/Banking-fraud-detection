def decide(score):
    if score <= 30:
        return "Approve", "Safe"
    elif score <= 70:
        return "Investigate", "Suspicious"
    else:
        return "Block", "Fraud"