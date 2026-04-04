def grade_hard(final_uptime: float, total_cost: float, info: dict) -> float:
    """
    Hard Task Grader: Stress Test & Recovery.
    AI ko sudden traffic spikes ke beech system ko zinda rakhna hai.
    """
    max_load = info.get("max_load", 0.0)
    score = 0.0

    # 1. Survival Check (Hard Constraint)
    # Agar uptime 99% se kam hai, toh AI seedha fail.
    if final_uptime < 99.0:
        return 0.0

    # 2. Stability under Stress (Weight: 0.6)
    # Agar max_load kabhi bhi 95% ke upar gaya, toh AI ne khatra mol liya.
    if max_load <= 85.0:
        score += 0.6 # Excellent handling of spikes
    elif max_load <= 95.0:
        score += 0.3 # Risky but survived
    else:
        score += 0.0 # Just barely survived

    # 3. Cost-Effective Scaling (Weight: 0.4)
    # Hard task mein thoda zyada cost allowed hai (Target: 40 units)
    if total_cost <= 40.0:
        score += 0.4
    elif total_cost <= 60.0:
        score += 0.2

    return round(min(1.0, max(0.0, score)), 2)
