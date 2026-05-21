# Write a Python program to calculate the factorial of a number provided by the
# user.


num=int(input("Enter your number:- "))
f=1
i=1


while i<=num:
    f=f*i
    i+=1
print("the fectorila of ",num, "is :- ", f )