# Write a Python program to generate a table of a number provided by the user.

# First Method
num1 = int(input("Enter Your number When you write table :- "))

for i in range(1,11):
    print(f"{num1} X {i} = {num1*i}")

# Secound Method

num=int(input("Enter Your Number :- "))
i=1

while i <11:
    print(f"{num} X {i} = {num*i}")
    i+=1