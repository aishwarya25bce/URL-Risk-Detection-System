# core/decision.py

def make_decision(score):
    """
    Convert risk score into decision label
    """

    if score >= 70:
        return {
            "label": "DO NOT CLICK 🚨",
            "level": "high"
        }

    elif score >= 40:
        return {
            "label": "SUSPICIOUS ⚠️",
            "level": "medium"
        }

    else:
        return {
            "label": "SAFE ✅",
            "level": "low"
        }