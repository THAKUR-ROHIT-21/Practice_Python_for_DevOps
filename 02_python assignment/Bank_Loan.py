# Bank Loan Approval System

# first method

age= int(input("Enter candidate age :- "))

if age >=18 and age <= 60:
    print(f"candidate  age is equal or greater than 18")
    monthly= int(input("Enter candidate Income in monthly :- "))
    if monthly >= 25000:
        print("candidate monthly is equal and greater than 25000 ")
        credit_score=int(input("Enter candidate credit score :- "))
        if credit_score >= 700:
            print("You are eligible for loan")
            outstanding_debt =float(input("Enter applicant's outstanding debt(rs):"))
            if outstanding_debt <=10000:
                print("outstanding is good")
            else:
                print("candidate outstanding is not clear")
        else:
            print("candidate not eligble becouse credit score is not greater than 700")
    else:
        print("candidate monthly is not full fil the bank cariteria ")
else:
    print("candidate not eligble becouse age is not greater than 18")


# Secound Method

age = int(input("Enter candidate age :- "))
monthly = int(input("Enter candidate Income in monthly :- "))
credit_score = int(input("Enter candidate credit score :- "))
outstanding_debt =float(input("Enter applicant's outstanding debt(rs):"))


if age >= 18 and age <= 60 and monthly >= 25000 and credit_score >= 700 and outstanding_debt<=10000:
    print("You are eligible for loan")
else:
    print("You are not eligible for loan")
 