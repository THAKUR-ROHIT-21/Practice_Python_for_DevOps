# 01. Tax Calculation for Car Purchase

brand = (input("Enter car brand(Mahindra,Audi,Jaguar,Mercedes: "))
price = float(input("Enter car price in lakhs: "))
tax = 0
if brand == "Mahindra" and 7 <= price <= 10:
    tax = price * 0.05
elif brand == "Audi" and 10 <= price <= 15:
    tax = price * 0.10
elif brand == "Jaguar" and 15 <= price <= 20:
    tax = price * 0.25
elif brand == "Mercedes" and 20 <= price <= 25:
    tax = price * 0.30
else:
    print("No tax applicable for this combination or invalid input.")
if tax > 0:
    print(f"Tax on your {brand} car is ₹{tax * 100000:.2f}")