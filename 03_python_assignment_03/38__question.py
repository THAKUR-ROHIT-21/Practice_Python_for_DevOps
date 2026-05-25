# Task: Print all characters from the string that are at odd indices.


string = input("Enter Your Value :-")

print("Characters at odd indices:")

for i in range(len(string)):
    if i % 2 != 0:   

        print(string[i])
