# 01.Profit and Loss percentage

cost_price = float(input("Enter Cost price of the Product :- "))
selling_price = float(input("Enter Selling price of the Product :- "))

profit = selling_price - cost_price
profit_p = (profit / cost_price) * 100

loss = cost_price - selling_price
loss_p = (loss / cost_price) * 100

if selling_price > cost_price:
    print(f"Profit :- {profit}")
    print(f"Profit Percentage :-{profit_p}\u0025")

elif cost_price > selling_price:
    print(f"Loss :- {loss}")
    print(f"Loss Percentage :- {loss_p}\u0025")

else:
    print("No Profit No Loss")

print("\n line")

