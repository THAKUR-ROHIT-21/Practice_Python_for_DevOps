# 01.Increase shopping cart items by 3 

cart_items1= 5
cart_items2=3
total_cart_items= cart_items1 +cart_items2 
print(total_cart_items)
print("_____________________________")

# 02. Apply a discount to a price 
#first method
price= 1000
discount= int(input("Enter your Discount Amount:-"))
afterdiscount= price*discount/100
print("Discount amount",afterdiscount)
print("_____________________________")

#secound method

price1= int(input("Enter product Amount:-"))
discount1= int(input("Enter your Discount Amount:-"))
afterdiscount1= price1*discount1/100
print(f"Product amount :- {price1} ")
print(f"Discount :- {discount1}%")
print(f"Discount amount:- {afterdiscount1}")
final_amount= price1-afterdiscount1
print(f"Final Payable Amount:- {final_amount}") #problum


