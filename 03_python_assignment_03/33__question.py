# 33.Replace Spaces with Underscores Replace all spaces in a string with underscores (_)

text = input("Enter a string:- ")

result = ""

for i in text:
    if i == " ":
        result += "_"
    else:
        result += i

print(result)


