# 19.Write a Python program to generate the pattern of the letter H.


n = 7 
for i in range(n):
    if i == n // 2:
        print('*' * n) 
    else:
        print('*' + ' ' * (n - 2) + '*')
        