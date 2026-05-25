# 32.Task: Replace Character in String
# Write a program that takes a string input from the user, then asks for a character
# to replace and the character to replace it with. The program should output the
# modified string where all occurrences of the specified character are replaced by
# the replacement character.

text = input("Enter a string:- ")
old = input("Character to replace:- ")
new = input("Replacement character:- ")

result = ""

for i in text:
    if i == old:
        result += new
    else:
        result += i

print(result)
