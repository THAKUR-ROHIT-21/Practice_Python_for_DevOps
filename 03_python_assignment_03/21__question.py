# 21.Write a Python program to display the squares of numbers from 1 to 10.

num1=int(input("Enter Your Number when you want to Square :- "))


for i in range(1, num1 + 1):
    print(i * i)


# Secound Method 

def square(a):
    for i in range(1, a +1 ):
        i*=i
    return i

num1=int(input("Enter Your Number when you want to Square :- "))
res=square(num1)
print(res)