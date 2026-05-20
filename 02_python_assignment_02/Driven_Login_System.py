msg="""chose the login option-
     1-login with phone
     2-login with email
     3-exit the system"""
print(msg)
login=int(input("Enter your choise"))
if(login==1):
    ph_num=str(input("Enter your number"))
    otp=str(input("Enter the otp"))
    if(ph_num=="1234567890" and otp=="1234"):
        print("login successfully")
    else:
        print("error")
elif(login==2):
    email=str(input("Enter email"))
    passd=str(input("Enter password"))
    if(email=="user@emaple.com" and passd=="password1234"):
        print("login successfull")
    else:
       print("Error")
else:
    print("Thank you")