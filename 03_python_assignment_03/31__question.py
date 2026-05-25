# 31.Count how many digits in the string are greater than 5 from text = "1234567890"

text = input("Enter Your Number :- ")
count = 0

for i in text:
    if i > "5":
        count += 1

print(count)