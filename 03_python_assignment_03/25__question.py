# 25.Given : 01275623
# Write a Python program to find and print the g character in the string.



s = "01275623"
g = s[0]

for i in s:
    if i > g:
        g = i

print("g iaracter is:", g)



