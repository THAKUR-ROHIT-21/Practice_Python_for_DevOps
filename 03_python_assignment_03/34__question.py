# 34.Remove Duplicate characters from the string given by the user then print the final
# output

s = input("Enter a string:- ")
result = ""

for i in s:
    if i not in result:
        result += i

print("Output:", result)
