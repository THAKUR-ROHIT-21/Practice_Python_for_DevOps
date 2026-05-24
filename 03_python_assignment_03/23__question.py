# 23.Given: text = "python programming"
# Goal: Count how many vowels are in the string. 
# Constraint: Do not use indexing (text[i]) or slicing (text[:]).

str1 = input("Enter Your string value :-")

v = "aeiouAEIOU"
count = 0

for i in str1: 
    if i in v:
        count += 1

print(count)