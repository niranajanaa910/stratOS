def analyze_market(goal: str):
    goal = goal.lower()

    if "price" in goal:
        return {
            "market_demand": "High",
            "competition": "Moderate",
            "recommendation": "Increase price by 5%"
        }

    elif "germany" in goal:
        return {
            "market": "Germany",
            "competition": "Medium",
            "customer_interest": "High",
            "recommendation": "Expansion looks feasible"
        }

    elif "launch" in goal:
        return {
            "trend": "Growing",
            "risk": "Medium",
            "recommendation": "Launch during Q4"
        }

    return {
        "recommendation": "No market insight found."
    }