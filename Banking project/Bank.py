from datetime import date 
from transaction_log import accountBalance

class Banking:
    global accountBalance
    global date
    
    def withdraw(amount):
        amount = float(amount)
        today = date.today()
        balance = accountBalance - amount
        f = open('transaction_log.py', 'a')
        f.write(f'log = \"WITHDRAWAL: On {today}, you withdrew {amount}, your newBalance is {balance}.\" \n')
        f.write(f'accountBalance = {balance} \n')
        f.close()
        return balance

    def deposit(amount):
        amount = float(amount)
        today = date.today()
        balance = accountBalance + amount
        f = open('transaction_log.py', 'a')
        f.write(f'log = \"DEPOSIT: On {today}, you deposited {amount}, your newBalance is {balance}.\" \n')
        f.write(f'accountBalance = {balance} \n')
        f.close()
        return balance

    def get_balance(self):
        return accountBalance

    run = True

    while run:
        action = input("Would you like to Deposit, Withdraw, or type 'get balance' to check the balance?: ")

        if action.lower() == "withdraw":
            amount = input('How much would you like to withdraw?: ')
            newBalance = withdraw(amount)
            print(f'You withdrew {amount}, your new balance is {newBalance}. Thank you!')
            accountBalance = newBalance

        elif action.lower() == "deposit":
            amount = input('How much would you like to deposit?: ')
            newBalance = deposit(amount)
            print(f'You deposited {amount}, your new balance is {newBalance}. Thank you!')
            accountBalance = newBalance

        elif action.lower() == "get balance":
            print(f'Your balance is {accountBalance}. Thank you!')




