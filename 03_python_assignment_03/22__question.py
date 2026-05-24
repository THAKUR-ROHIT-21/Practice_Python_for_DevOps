# 22.Given a string text = "python", calculate the sum of the indices of its
# characters without using the range() or len() functions.

str1 = input("Enter String Value :- ")

p = 0
t = 0

for i in str1:
    t += p
    p += 1

print(t)

# Secound Method

def indices(a):
    t=0
    p=0
    for i in a:
        p+=t
        t+=1
    return p


str1=input("Enter Your String Value :- ")
res=indices(str1)
print("sum of the indices :-",res)







