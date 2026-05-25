# 40.Count how many digits in a string entered by the user.
# text=”sytax_error2806 hai ”


str1 = input("Enter string Value :-")
c = 0

for i in str1:
    if '0' <= i <= '9':
        c += 1

print("Number of digits:-", c)
