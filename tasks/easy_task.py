def grade_easy(final_uptime: float, total_cost: float, info: dict) -> float:
    max_load = info.get("max_load", 0.0)
    score = 0.0

    # 1. Uptime Score (Main Goal) - 70% Weight
    score += (final_uptime / 100.0) * 0.7

    # 2. Stability Score - 30% Weight
    if max_load < 75.0:
        score += 0.3
    elif max_load < 90.0:
        score += 0.15
    
    # 3. Efficiency Penalty (Naya Badlaw!)
    # Agar AI ne 10 se zyada servers khade kar diye easy task mein
    if total_cost > 50.0:
        score -= 0.1 

    return round(min(1.0, max(0.0, score)), 2)
