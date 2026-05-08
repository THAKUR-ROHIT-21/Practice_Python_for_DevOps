# 01. Student Grading System


user= int(input("Enter your marks :- "))

if user >= 90 and user <= 100:
    print("your Grade is A ")
elif user >= 80 and user <= 89:
    print("your grade is B")
elif user >= 70 and user <= 79:
    print("your grade is C")
elif user >= 60 and user <= 69:
    print("your grade is D")
elif user >= 50 and user <= 59:
    print("your grade is E")
elif user >= 40 and user <= 49:
    print("your grade is F ")
else:
    print("Invalid marks")