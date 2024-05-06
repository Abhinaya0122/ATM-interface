class ATM():
    def __init__(self):
        self.users={}
    def add_user(self,user):
        self.users[user.user_id]=user
    def authenticate_user(self,user_id,pin):
        if user_id in self.users and self.users[user_id].pin==pin:
            return self.users[user_id]
        else:
            return None
    def check_user(self,user_id):
        if user_id in self.users :
            return self.users[user_id]
        else:
            return None

    def display_transaction_history(self,user):
        for transactions in user.transaction_history:
            print(transactions)


class User:
    def __init__(self,user_id,pin,balance):
        self.user_id=user_id
        self.pin=pin
        self.balance = balance
        self.transaction_history=[]

    def withdraw(self,amount):
        if(amount>=self.balance):
            print("Insufficient balance")
        else:
            self.balance -=amount
            self.transaction_history.append(f'Withdraw amount {amount} . Available balance {self.balance}')
    
    def deposit(self,amount):
        self.balance +=amount
        self.transaction_history.append(f'Deposit amount {amount}. Available balance: {self.balance}')

    def transfer(self,recepient,amount):
        if self.balance<=amount:
            print('Insufficient balance')
            return False
        else:
            self.balance -= amount
            recepient.balance += amount
            self.transaction_history.append(f'Transfer to {recepient.user_id}: {amount}')
            recepient.transaction_history.append(f'Transfer from {self.user_id}: +${amount}')
            return True
        

atm=ATM()
def create_new_user():
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")
    balance = float(input("Enter initial balance: "))
    return User(user_id, pin, balance)


num_users = int(input("How many users do you want to create? "))
for _ in range(num_users):
    user = create_new_user()
    atm.add_user(user)

authenticated_user = None
while not authenticated_user:
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")
        authenticated_user = atm.authenticate_user(user_id, pin)
        if not authenticated_user:
            print("Invalid user ID or PIN. Please try again.")

while(True):
    need = int(input("Codes 1:deposit\n 2:withdraw\n 3:Check balance\n 4:Show transaction history\n 5:Transfer\n 6:Quit\n Enter code: "))
    if need ==1:
        amt = int(input("Enter the amount to be deposited: "))
        authenticated_user.deposit(amt)
        print("Current balance:", authenticated_user.balance)
    elif need==2:
        amt = int(input("Enter the amount to be withdraw: "))
        authenticated_user.withdraw(amt)
        print("Current balance:", authenticated_user.balance)
    elif need == 3:
        print("Current balance:", authenticated_user.balance)
    elif need == 4:
        print('Transaction history: ',authenticated_user.transaction_history)
    elif need == 5:
        user_id = input("Enter user ID: ")
        recepient=atm.check_user(user_id)
        amt = int(input("Enter the amount to be transfered: "))
        authenticated_user.transfer(recepient,amt)
        print("User balance:", authenticated_user.balance)
        print("Recepient balance:", recepient.balance)

    elif need==6:
        break

    else:
        print('Enter the valid no')
