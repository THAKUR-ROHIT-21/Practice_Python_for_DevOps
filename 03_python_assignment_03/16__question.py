# 16.Write a Python program to filter out all vowels and consonants from a string
# entered by the user.

str1=input("Enter Your String value :- ")

for i in str1:
    if i in "aeiouAEIOU":
        print("vowel is :- ",i)
    else:
        print("consonants :- ",i)

# Secound Method

def v_c(a):
    for i in a:
        if i in "aeiouAEIOU":
            print("vowel is :- ",i)
        else:
            print("consonants :- ",i)

str1=input("Enter Your String value :- ")
v_c(str1)





