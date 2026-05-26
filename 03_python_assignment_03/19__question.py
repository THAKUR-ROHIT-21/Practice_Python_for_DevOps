# 19.Write a Python program to generate the pattern of the letter H.

# n = 7 
# for i in range(n):
#     if i == n // 2:
#         print('*' * n) 
#     else:
#         print('*' + ' ' * (n - 2) + '*')


# Secound Method 


n = int(input("Enter Your Number :- "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )

        