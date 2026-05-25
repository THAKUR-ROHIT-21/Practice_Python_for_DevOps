# 29.Take two numbers from the user: start and end. Print a string labeling each
# number in that range as Odd or Even.


start=int(input("Enter Your First Number :- "))
end=int(input("Enter Your Secound Number :-"))

for i in range(start,end+1):
    if i%2==0:
        print(f"Even number :-{i} \n")
        continue
    else:
        print(f"Odd Number:- {i} \n")