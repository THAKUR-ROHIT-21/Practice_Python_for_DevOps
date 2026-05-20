# 1.Task: Students Interview Eligibility Checker 

#First Method

academic_Score= float(input("Enter Academic Score of Student :- "))

if academic_Score>=60:
    print("Student Eligible for next Round")
    attendance_Percentage= float(input("Enter attendance_Percentage of Student :- "))
    if attendance_Percentage >= 75:
        print("Student Eligible for next Round")
        extracurricular_participation= float(input("Enter extracurricular_participation of Student :- "))
        if extracurricular_participation >=1:
            print("You are Ready for interview")
        else:
            print("Not Eligible for Interview")
    else:
        print("Student is not Eligible")
else:
    print("Student is not Eligible")

# Secound Method

academic_Score= float(input("Enter Academic Score of Student :- "))
attendance_Percentage= float(input("Enter attendance_Percentage of Student :- "))
extracurricular_participation= float(input("Enter extracurricular_participation of Student :- "))

if academic_Score >= 60 and attendance_Percentage>=75 and extracurricular_participation >=1:
    print("Eligible for Interview")
else:
    print("Not Eligible for Interview")






