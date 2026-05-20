# 01.Task: Retirement Age Calculatand

# first Method

Player1=int(input("Enter Your Run fand first player1 :- "))
Player2=int(input("Enter Your Run fand first player2 :- "))
Player3=int(input("Enter Your Run fand first player3:- "))
Player4=int(input("Enter Your Run fand first player4 :- "))
Player5=int(input("Enter Your Run fand first player5 :- "))

total_player=5
total_run= Player1+Player2+Player3+Player4+Player5
average= total_run/total_player

print(f"Totaol Run:- {total_run}")
print(f"Average of players run :- {average}")

# Secound Method

Player6=int(input("Enter first player Run :- "))
Player7=int(input("Enter Secound player Run :- "))
Player8=int(input("Enter Third player Run :- "))
Player9=int(input("Enter Forth player Run :- "))
Player10=int(input("Enter Fifth Run :- "))

if Player6>Player7 and Player6>Player8 and Player6>Player9 and Player6>Player10:
    print("Pleyar one is well played in own Tean")
elif Player7>Player6 and Player7>Player8 and Player7>Player9 and Player7>Player10:
    print("Pleyar Two is well played in own Tean")
elif Player8>Player6 and Player8>Player7 and Player8>Player9 and Player8>Player10:
    print("Pleyar Three is well played in own Tean")
elif Player9>Player6 and Player9>Player7 and Player9>Player8 and Player9>Player10:
    print("Pleyar Four is well played in own Tean")
else:
    print("Player five is well player in own Team")

