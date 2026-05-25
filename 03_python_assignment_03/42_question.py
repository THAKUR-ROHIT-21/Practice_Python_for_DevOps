# 42.You are managing a simple banking system that tracks the balance at the end of
# each day over 10 days. Each day, the balance increases by 100 units starting from 100
# on day 1, 200 on day 2, and so on. You want to print the current day’s balance along with
# the previous day’s balance. For day 1, the previous day’s balance is 0.

day=int(input("Enter the number of the day:-"))
a=0
count=0
for i in range (1,day+1):
    a+=100
    count+=1
    print(f"Day {count}: Balance = {a}, Previous Day Balance = {a-100}")
print(f"Total Balance = {a}")