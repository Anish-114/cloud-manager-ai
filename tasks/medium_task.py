def grade_medium(final_uptime: float, total_cost: float, info: dict) -> float:
    """
    Medium Task Grader: Cost Optimization & Efficiency.
    AI ko score tabhi milega jab system crash na ho aur budget kam rahe.
    """
    score = 0.0
    
    # 1. Critical Failure Check
    # Agar uptime 95% se kam hai, toh AI seedha fail (0.0 score)
    if final_uptime < 95.0:
        return 0.0

    # 2. Uptime Performance (Weight: 0.5)
    # 100% uptime = 0.5 points
    score += (final_uptime / 100.0) * 0.5

    # 3. Cost Efficiency (Weight: 0.5)
    # Target Cost: Hum chahte hain cost 15 units se kam rahe
    # Agar cost 15 ya usse kam hai, toh full 0.5 points
    if total_cost <= 15.0:
        score += 0.5
    # Agar cost 30 tak hai, toh thode kam points (0.2)
    elif total_cost <= 30.0:
        score += 0.2
    # Agar bahut zyada kharcha kiya (Cost > 30), toh efficiency points 0
    else:
        score += 0.0

    return round(min(1.0, max(0.0, score)), 2)
