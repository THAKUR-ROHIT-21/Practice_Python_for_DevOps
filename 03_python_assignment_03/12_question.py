# Write a Python program to reverse a string entered by the user.

str1= input("Enter your reverse a string :- ")

rev= " "

for i in str1:
    rev=i+rev
print("Reversed string :-", rev)


# secound 


text = input("Enter a string: ")
reversed_text = ""

i = len(text) - 1

while i >= 0:
    reversed_text += text[i]
    i -= 1

print("Reversed string:", reversed_text)
