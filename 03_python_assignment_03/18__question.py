# 18.Write a Python program to display all possible pairs of 3.
# Example: 1:3, 2:3, 3:3 , 2:1 , 2:2 ,2:3 , 3:1 ,3:2 ,3:3

# First Method 
num1=int(input("Enter Your Number :- "))
for i in range(1, num1):
    for j in range(1, num1):
        print(f"{i}:{j}")

# Secound 

def pair(a):
    for i in range(1,a):
        for j in range(1,a):
            return (f"{i}:{j}")

num1=int(input("Enter Your Number :- "))
res=pair(num1)
print(res)

