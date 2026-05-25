# 35.Take string from user and Replace every vowel in the string with an asterisk *.




text = input("Enter a string: ")

vowels = "aeiouAEIOU"
result = ""

for i in text:
    if i in vowels:
        result += "*"
    else:
        result += i

print("Modified string:", result)