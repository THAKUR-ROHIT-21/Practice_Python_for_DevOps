# 1.Calculate perimeter of a square 
# first method

side = 9
perimeter= side*4

print(perimeter)
print("-"*50)

# Secound method 
side1=int(input("Enter number:- "))
perimeter1= side1*4

print(f"Number of perimeter:- {perimeter1}")
print("-"*50)

# 2.Calculate diameter of a circle 

dia_redus= int(input("Enter diametar of a circle:- "))
diameter = dia_redus*2
print(f"Diameter is :- {diameter}")
print("-"*50)

# 3. Calculate volume of a cube 

cube_side = int(input("Enter Side value:- "))
value_cube= cube_side**3

print(f"Valume of Cube:- {value_cube}")
print("-"*50)

# 4.Calculate surface area of a cuboid 

L= int(input("Enter value of lenght:- "))
B= int(input("Enter valueof base:- "))
H= int(input("Enter value of Height:- "))

Surface_area= ((L*B)+(B*H)+(H*L))
area_s= 2*Surface_area

print(f"Surface of Area:- {area_s}")
print("-"*50)