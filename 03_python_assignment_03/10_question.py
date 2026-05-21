# Write a Python program to display all letters except 'm' and 'i' from the string
# "Dreamer infotech".


str1= input("Enter Your String :- ")

for i in str1:
    if i =="m" or i=="i" or i=="M" or i=="I":
        continue
    print(i,end=" ")

else:
    print("not any miMI here")