# 15.Write a Python program that allows the user to search for a character within a
# given string

# first method

str1=input("Enter your string :- ")
str2=input("Enter your search character :- ")

for i in str1:
    if i == str2:
        print("Yes the character is available ")
        break
else:
    print("No the character is not available")

# Secound method

def char(a,b):
    for i in a:
        if i == b:
            return ("Yes the character is available ")
        break
    else:
        return ("No the character is not available")

str1=input("Enter your string :- ")
str2=input("Enter your search character :- ")
res=char(str1,str2)
print(res)

