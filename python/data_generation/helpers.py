"""
Helper Functions
----------------
Reusable business logic for the AI Marketing Campaign
Intelligence Platform.
"""

import random
from datetime import date, timedelta


# ==========================================================
# Budget Category
# ==========================================================

def get_budget_category(budget: int) -> str:

    if budget < 100000:
        return "Small"

    elif budget < 500000:
        return "Medium"

    elif budget < 1000000:
        return "Large"

    return "Enterprise"


# ==========================================================
# AI Campaign Score
# ==========================================================

def generate_ai_score(budget: int) -> int:

    if budget >= 1000000:
        return random.randint(85, 100)

    elif budget >= 500000:
        return random.randint(75, 95)

    elif budget >= 100000:
        return random.randint(60, 90)

    return random.randint(45, 80)


# ==========================================================
# Success Probability
# ==========================================================

def generate_success_probability(ai_score: int) -> float:

    probability = ai_score + random.randint(-8, 8)

    probability = max(35, probability)

    probability = min(99, probability)

    return round(probability, 2)


# ==========================================================
# Risk Level
# ==========================================================

def get_risk_level(ai_score: int) -> str:

    if ai_score >= 85:
        return "Low"

    elif ai_score >= 70:
        return "Medium"

    return "High"


# ==========================================================
# Campaign Priority
# ==========================================================

def get_priority(ai_score: int) -> str:

    if ai_score >= 90:
        return "High"

    elif ai_score >= 70:
        return "Medium"

    return "Low"


# ==========================================================
# Expected ROI
# ==========================================================

def generate_expected_roi(ai_score: int) -> float:

    roi = ai_score * random.uniform(0.8, 1.5)

    return round(roi, 2)


# ==========================================================
# Campaign Duration
# ==========================================================

def generate_campaign_duration() -> int:

    return random.randint(15, 120)


# ==========================================================
# Campaign Dates
# ==========================================================

def generate_campaign_dates(status, duration):

    today = date.today()

    if status == "Completed":

        end_date = today - timedelta(
            days=random.randint(5, 90)
        )

        start_date = end_date - timedelta(
            days=duration
        )

    elif status == "Running":

        start_date = today - timedelta(
            days=random.randint(5, duration)
        )

        end_date = start_date + timedelta(
            days=duration
        )

    else:

        start_date = today + timedelta(
            days=random.randint(5, 60)
        )

        end_date = start_date + timedelta(
            days=duration
        )

    return start_date, end_date