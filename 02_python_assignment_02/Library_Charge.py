# 01.Library Charge Calculation

day=int(input("Enter number of days the book has been borrowed:"))
if(day<=15):
    if(day>5):
        if(day>10):
            price=5*2+5*3+(day-10)*4
            print(price)
        else:
            price=5*2+(day-5)*3
            print(price)
    else:
        price=day*2
        print(price)
else:
    price=5*2+5*3+5*4+(day-15)*5
    print(price)