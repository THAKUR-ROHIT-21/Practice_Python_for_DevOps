# 27.Give : text=”if you think you can not do, you can not show think wisely”
# Goal: Print the alternate words
# Constraint: Do not use space between words more than once .

text = "if you think you can not do, you can not show think wisely"

w = ""
count = 0

for i in text + " ":
    if i != " ":
        w += i
    else:
        if count % 2 == 0:
            print(w, end=" ")
        w = ""
        count += 1