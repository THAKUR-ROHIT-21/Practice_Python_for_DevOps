# 37.Task: Count how many uppercase and lowercase letters are in a string.



string = input("Enter Your Value :- ")
u = 0
l = 0

for i in string:
    if 'A' <= i <= 'Z':
        u += 1

        
    elif 'a' <= i <= 'z':
        l += 1

print("Uppercase letters:", u)
print("Lowercase letters:", l)
