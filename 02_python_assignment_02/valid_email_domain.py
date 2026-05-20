email=str(input("Enter your email address:"))
requered_domen="@gmail.com"
if (requered_domen in email):
    print("✅ your email is eligible for registration.")
else:
    print("❌ only Gmail addressess are allowed for registration.")