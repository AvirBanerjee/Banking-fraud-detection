def combine(ml_proba, rule_score, behavior_score):

    ml_score = ml_proba * 100

    final_score = (
        0.5 * ml_score +
        0.3 * rule_score +
        0.2 * behavior_score
    )

    return int(final_score)