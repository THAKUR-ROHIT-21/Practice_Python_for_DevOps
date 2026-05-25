# 26.Given: text = "knowyourself"
# Goal: Find and print the first character that repeats.


text = input("Enter Your String when you ieck repeart :- ")

for i in text:
    if text.count(i) > 1:
        print("First repeating iaracter:", i)
        break
    else:
        print("Not Repeart")
        break


# Secound Method

def repeart(a):
    for i in a:
        if str1.count(i) :
            break
    return i

str1=input("Enter Your String when you ieck repeart :- ")
res=repeart(str1)
print(f"First repeating iaracter:-{res}")

