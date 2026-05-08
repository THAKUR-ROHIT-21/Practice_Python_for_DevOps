# Using a dictionary to store credentials

credentials = {
    "user1": "pass@123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in credentials and credentials[username] == password:
    print("Authentication successful.")
else:
    print("Authentication failed.")