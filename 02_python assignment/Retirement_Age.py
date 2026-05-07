# 1. Task: Retirement Age Calculator
# ● Objective: Write a program that prompts the user for their age and tells them how
# many years until they reach retirement age (65).
# ● Hints:
# ○ Ask the user to input their age.
# ○ Calculate how many more years they have until they reach 65 years of
# age.
# ○ Display the number of years left until retirement or a message if the user
# has already reached retirement age.

age= int(input("Enter Your Age :- "))
retirement_age=65
years_left= retirement_age - age

if age<retirement_age:
    print(f"you have {years_left} years left until retirement at age {retirement_age}.")
elif age==retirement_age:
    print("congratulations! you are at the retirement age.")
else:
    print("you have already reached retirement age.")




