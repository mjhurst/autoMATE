import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Check for both uppercase and lowercase characters
    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        return "Password should contain both uppercase and lowercase characters."

    # Check for digits
    if not any(c.isdigit() for c in password):
        return "Password should contain at least one digit."

    # Check for special characters
    if not re.search(r'[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:\'",<>\./?\\|]', password):
        return "Password should contain at least one special character."

    return "Password is strong and meets the criteria."


def main():
    print("Verify your password stength")
    password = input("Enter a password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
