# 1.If user input is: 

#first method
print("First method")

user_name= str(input("Enter your name:- "))
user_age= int(input("Enter your age:- "))
user_city=str(input("Enter your city name:- "))
user_hobby= str(input("Enter your hobby:-"))

print(f"Your name :- {user_name}")
print(f"Your age :- {user_age}")
print(f"Your City :- {user_city}")
print(f"Your hobby :- {user_hobby}")
print()

print(f"Meet {user_name}, a {user_age}-year-old enthusiast from {user_city}.")
print( f"When not busy with daily tasks, {user_name} loves spending time {user_hobby}.") 
print(f"Life in {user_city} keeps {user_name} energetic and curious every single day. ")
print(f"With coding as a passion, the future looks creative and inspiring for") 
print(f"{user_name} in the {user_city} City. ")
print("_"*50)

# Secound method
print("Secound Method")

User = {
    "name": "Rohit Kr Thakur",
    "age": 24,
    "city": "Siwan",
    "hobby": "Reading"
}
print()

print(f"Meet {User['name']}, a {User['age']}-year-old enthusiast from {User['city']}.")
print( f"When not busy with daily tasks, {User['name']} loves spending time {User['hobby']}.") 
print(f"Life in {User['city']} keeps {User['name']} energetic and curious every single day. ")
print(f"With coding as a passion, the future looks creative and inspiring for") 
print(f"{User['name']} in the {User['city']} City. ")
