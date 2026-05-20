# Task : Authentication System

username1 = "user1"
username1_password1 = "pass@123"

enterName = input("Enter your username:")
enterPassword = input("Enter your password:")

if enterName == username1 and enterPassword ==username1_password1:
    print("You are succesesful login")
else:
    print("Authentication failed re-enter your userName or password")
