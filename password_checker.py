import re

def assess_password(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    score = sum(criteria.values())
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Medium"
    else:
        strength = "Weak"
    return strength, criteria
