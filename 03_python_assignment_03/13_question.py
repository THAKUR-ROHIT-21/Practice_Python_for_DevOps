# 13.Write a Python program to count the total number of characters in a string
# entered by the user.

# first Method

str1=input("Put the string value to count :- ")
c=0


for i in str1:
    c+=1
print(f"Total number of characters:- {c}")

# Secound method

def char(a):
    c=0
    for i in a:
        c+=1        
    return c

str1=input("Put the string value to count :- ")
res=char(str1)
print(f"Total number of characters:- {res}")

