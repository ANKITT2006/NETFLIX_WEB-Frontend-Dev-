account = 10012738545
balance = 25000

print("1.deposit")
print("2.withdraw")
print("3.current balance")

choice=int(input("enter your choice:"))

if choice==1:
    deposit_amount=int(input("enter the deposit_amount:"))
    total_balance=balance+deposit_amount
    print(f"the total balance is {total_balance} in account {account}")
elif choice==2:
    withdraw_amount=int(input("enter the withdraw_amount:"))
    total_balance=balance-withdraw_amount
    print(f"the total balance is {total_balance} in account {account}")
elif choice==3:
    print(f"the current balance is {balance} in account {account}")
    
else:
    print("invalid input")
    