# 01.Arranging Three Numbers in Descending Order


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")


numbers = [num1, num2, num3]
numbers.sort(reverse=True)
print(f"Numbers in Descending Order :- {numbers}")
