# 01. Calculate Class Attendance Percentage

classes= int(input("Enter the total number of classes held: "))
attended= int(input("Enter the number of classes attended: "))

attendance_percentage= (attended / classes) * 100

if attendance_percentage >= 75:
    print("Eligible to sit in the exam.")
else:
    print("Not eligible to sit in the exam.")

print(f"\nAttendance Percentage: {attendance_percentage:.2f}%")