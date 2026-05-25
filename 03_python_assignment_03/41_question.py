# 41.Count only alphabets (both uppercase and lowercase).
# Enter a string: this123 i am
# Number of letters: 7




s = input("Enter Your Valur :-")
count = 0

for c in s:
    if ('A' <= c <= 'Z') or ('a' <= c <= 'z'):
        count += 1

print("Number of letters:", count)

