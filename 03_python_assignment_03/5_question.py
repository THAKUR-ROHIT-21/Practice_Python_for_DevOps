# 5. Write a Python program to calculate the sum of numbers between a starting and
# ending point provided by the user.


start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

t = 0

for i in range(start, end + 1):
    t+= i

print("Sum =", t)



