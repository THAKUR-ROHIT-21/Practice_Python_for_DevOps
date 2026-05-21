# Write a Python program to generate the Fibonacci sequence up to a specified
# number of terms.


num1 = int(input("Enter the number of terms: "))

a=0
b=1
i=0

while i<=num1:
    print("Fibonacci number is : -" ,i)

    a=b
    b=i
    i=a+b

