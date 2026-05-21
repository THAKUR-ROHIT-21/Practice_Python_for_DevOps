# Write a Python program to calculate the product of numbers between a starting
# and ending point provided by the user.

start = int(input("Enter your product number :- "))
end = int(input("Enter your product number :- "))

for i in range(start+1,end+1):
    start *= i

print("product number is :- ",start)