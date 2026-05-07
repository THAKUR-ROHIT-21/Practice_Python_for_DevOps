# 4. Task: Calculate the Area of a Circle
# ● Objective: Write a program to calculate the area of a circle.
# ● Hints:
# ○ Ask the user to input the radius of the circle.
# ○ Calculate the area of the circle using the formula: Area = π *
# radius^2.
# ○ Display the calculated area.
# First method 
value= float(input("Enter Redius of circle :-  "))
squre= value**2
π= 3.14
area= squre*π
print(f"Area of circle :- {area}")
print("_"*100)

# Secound Method
# exact value of π
import math

value1= float(input("Enter Radius of circle :- "))

if value1>0:
    area = math.pi * (value1 ** 2)
    print(f"Area of the circle :- {area}")
else:
    print("Radius is less than 0 ")


