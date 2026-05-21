# 4. Write a Python program to check if a number provided by the user is prime or not.

num1 = int(input("Enter Your Number :- "))

if num1 > 1:
    for i in range(2, num1):
        if num1 % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("This is Prime Number")
else:
    print("Not a Prime Number")
