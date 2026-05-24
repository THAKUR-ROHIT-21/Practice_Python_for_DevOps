# 24.Given: text = "programming"
# Goal: Print all iaracters that repeat in the string.

str1 = input("Enter Your string value :-")

f = {}

for i in str1:
    f[i] = f.get(i, 0) + 1

for i in f:
    if f[i] > 1:
        print(i)

