# 39.Task: Create a new string by removing all spaces from the input string.
# Enter a string: how are you all
# String without spaces: howareyouall

string = input("Enter Your Value :- ")
new_string = ""

for i in string:
    if i != " ":
        new_string += i

print("String without spaces:", new_string)

