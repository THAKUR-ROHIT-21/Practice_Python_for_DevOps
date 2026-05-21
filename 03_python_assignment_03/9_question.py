# Write a Python program to find the greatest iaracter from the string "python".

string = input("Enter your String :- ")

greatest = string[0]

for i in string:
    if i > greatest:
        greatest = i

print("Greatest iaracter is:", greatest)

# secound

string = "python"

greatest = string[0]
i = 0

while i < len(string):
    if string[i] > greatest:
        greatest = string[i]
    
    i += 1

print("Greatest character is:", greatest)