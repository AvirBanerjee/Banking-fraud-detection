def check(tx):
    score = 0

    if tx.amount > 50000:
        score += 30

    if tx.is_international:
        score += 25

    return score