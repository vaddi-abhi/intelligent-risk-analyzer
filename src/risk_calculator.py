# src/risk_calculator.py

def calculate_risk_score(
    vulnerabilities,
    dependencies,
    license_risk
):

    score = 0

    vulnerability_count = len(
        vulnerabilities
    )

    dependency_count = len(
        dependencies
    )

    score += vulnerability_count * 5

    if dependency_count > 10:
        score += 5

    elif dependency_count > 5:
        score += 3

    if license_risk == "High":
        score += 5

    elif license_risk == "Medium":
        score += 2

    return score


def get_risk_level(score):

    if score <= 5:
        return "Low"

    if score <= 10:
        return "Medium"

    if score <= 15:
        return "High"

    return "Critical"
