# Edit valid credentials to meet your needs
valid_credentials = {
    "user1": "password123",
    "user2": "securepwd456",
    "user3": "letmein789",
}

def authenticate(username, password):
    if username in valid_credentials and valid_credentials[username] == password:
        return True
    return False

def main():
    print("User Authentication")
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if authenticate(username, password):
            print("Authentication successful. Welcome, " + username + "!")
            break
        else:
            print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()