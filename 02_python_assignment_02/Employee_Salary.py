# 01.Employee Salary Based on Experience.

experience = int(input("Enter year experience: "))

if experience >= 10:
    print("Senior employee")
    salary = 80000
    if experience > 15:
        print("Experience exceeds 15 years. Bonus added.")
        salary += 5000
    print("Salary:", salary)

elif experience >= 5:
    print("Mid-level employee")
    salary = 50000
    print("Salary:", salary)

else:
    print("Junior employee")
    salary = 30000
    print("Salary:", salary)