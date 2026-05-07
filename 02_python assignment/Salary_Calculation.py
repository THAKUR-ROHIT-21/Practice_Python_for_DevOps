# 1. Task: Salary Calculation

base_salary = 50000
bonus = 5000
tax_rate =0.10
other_charges =2000

gross_salary = base_salary +bonus
tax = gross_salary * tax_rate
net_salary = gross_salary-tax-other_charges

print(f"gross salary:- {gross_salary}rs")
print()
print(f"tax (10%):- {tax}rs")
print()
print(f"other charges:- {other_charges}rs")
print()
print(f"net salary:- {net_salary}rs")
print("_"*100)
