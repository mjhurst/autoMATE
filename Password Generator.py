import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

def main():
    print("Password Automation Script")
    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. Save a password to a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            password_length = int(input("Enter the desired password length: "))
            password = generate_password(password_length)
            print("Generated Password:", password)
        elif choice == '2':
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password_to_file(username, password)
            print("Password saved to 'passwords.txt'")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()