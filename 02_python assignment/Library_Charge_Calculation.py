# 01.Library Charge Calculation

# Input number of days the book is borrowed
days = int(input("Enter number of days the book is borrowed: "))
charge = 0

if days <= 5:
    print(f"Total library charges:- {days * 2}")
elif days <= 10:
    print(f"Total library charges :- {(5 * 2) + (days - 5) * 3}")
elif days <= 15:
    print(f"Total library charges :- {(5 * 2) + (5 * 3) + (days - 10) * 4}")
else:
    print(f"Total library charges :- {(5 * 2) + (5 * 3) + (5 * 4) + (days - 15) * 5}")


