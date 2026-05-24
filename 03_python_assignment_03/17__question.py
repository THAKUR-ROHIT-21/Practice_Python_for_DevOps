# 17.Write a Python program to filter out duplicate iacters from a string entered by
# the user


str1 = input("Enter a string :- ")

res = ""

for i in str1:
    if i not in res:
        res += i

print("String after removing duplicate iacters:", res)

# Secound Method 

def char(a):
    r=""
    for i in a:
        if i not in r:
            r+=i
            return r
    
str1 = input("Enter a string :- ")
res=char(str1)
print("String after removing duplicate iacters:",res)




