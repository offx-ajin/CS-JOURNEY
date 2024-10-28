'''
Author : Ajin Saji
Date :28/10/24
Description: a program that simulates a simple bank ATM system
'''
balance_amount=1000
while True:
    print("1.\tCheck balance")
    print("2.\tDeposit money")
    print("3.\tWithdraw money")
    print("4.\tExit")
    choice=int(input("enter your choice:"))
    if choice ==1:
        print(f"The current balance ${balance_amount}")
    elif choice ==2:
        deposit_amount = float(input("enter the amount:"))
        balance_amount= deposit_amount +balance_amount
        print(f"The deposited amount ${deposit_amount} and " f"the current balance is ${balance_amount}")

    elif choice ==3:
        withdraw_amount= float(input("enter the amount:"))
        balance_amount= balance_amount-withdraw_amount
        if withdraw_amount>balance_amount:
            print("insufficeint balance")
        else:
             print(f"The withdrawed amount ${withdraw_amount} and" f"The current balance is $ {balance_amount}")
    elif choice ==4:
        break
    else:
        print("invalid entry")

