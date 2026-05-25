# 20.Write a Python program to find deplicate letters between two strings.
# Example: In "virat" and "rohit", the dep letter is "r".

str1 = input("Enter first string :- ")
str2 = input("Enter second string :- ")

dep = ""

for i in str1:
    if i in str2 and i not in dep:
        dep += i

print("deplicate letters are:-", dep)


# Secound Method

def dep(a,b):
    dep=""
    for i in a:
        if i in b and i not in dep:
            dep += i
        return dep

str1 = input("Enter first string :- ")
str2 = input("Enter second string :- ")
res=dep(str1,str2)
print("deplicate letters are:-",res)



