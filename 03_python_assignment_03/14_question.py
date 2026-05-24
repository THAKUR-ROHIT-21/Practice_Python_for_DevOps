# 14.Write a Python program to check whether a string entered by the user is a
# palindrome.

# first method 

str1=input("Enter Your any string :- ")

rev= ""

for i in str1:
    rev=i+rev

if str1 == rev:
    print("This is Palindrome")
else:
    print("This isn't Palindrome")

# Secound method 

def palindrome(a):

    rev=""
    for i in a:
        rev=i+rev
    if a==rev:
        return "This is palindrome"
    else:
        return "This isn't palindrome"


str2=input("Enter Your any String : -")
res=palindrome(str2)
print(res)








