from password_checker import assess_password
from feedback import generate_feedback

def main():
    print("==== Password Complexity Checker ====")
    password = input("Enter a password to assess: ").strip()
    strength, criteria = assess_password(password)
    print(f"\nPassword Strength: {strength}")
    print(generate_feedback(strength, criteria))

if __name__ == "__main__":
    main()
