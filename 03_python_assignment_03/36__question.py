# 36.Count only words not spaces.
# Entered a string: Hello coders from Success24
# Number of words: 4

string = input("Enter Your Value :- ")
c=1

for i in string:
    if i == " ":
        c += 1

print("Number of words:", c)



