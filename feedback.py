def generate_feedback(strength, criteria):
    feedback = []
    if strength == "Strong":
        return "Your password is strong. Great job!"
    if not criteria["length"]:
        feedback.append("Use at least 8 characters.")
    if not criteria["uppercase"]:
        feedback.append("Add at least one uppercase letter (A-Z).")
    if not criteria["lowercase"]:
        feedback.append("Add at least one lowercase letter (a-z).")
    if not criteria["digit"]:
        feedback.append("Add at least one number (0-9).")
    if not criteria["special"]:
        feedback.append("Include special characters (e.g., @, #, $, etc.).")
    return " ".join(feedback)
