class BankAccount:
    Bank_Name = 'Dojo_Ninja Bank'
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here
    def display_account_info(self):
        print(f'Account info - Interest Rate:{self.int_rate} Balance:{self.balance}')
        return self
        # your code here
    def yield_interest(self):
        interest = (self.int_rate * self.balance)
        self.balance = interest + self.balance
        print(f'The Interest is: {interest}')
        return self 
        # your code here
    @classmethod
    def all_acnt(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls
        
saving = BankAccount(.04,100)
checking = BankAccount(.05,50)
    
# saving.deposit(500).deposit(200).deposit(50).withdraw(600).yield_interest().display_account_info()
# checking.deposit(500).deposit(500).withdraw(60).withdraw(200).withdraw(100).withdraw(50).yield_interest().display_account_info()
# BankAccount.all_acnt()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.03, balance=0)
    # other methods
        self.savings = BankAccount( int_rate=0.02,balance=0)
    def make_deposit(self, amount,amount2):
        self.account.balance += amount
        self.savings.balance += amount2
        return self
        
    def make_withdrawal(self, amount,amount2):
        self.account.balance -= amount
        self.savings.balance -= amount2
        return self
    
    def transfer_money(self, amount, other_user):
        

        return self
    
    def display_user_balance(self):
        print(f'Name: {self.name}\nEmail: {self.email}\nChecking: {self.account.balance}\nSavings: {self.savings.balance}')
        return  self
        
kevin = User('Kevin', 'lily@gmail.com').make_deposit(200,20).display_user_balance()
ryan = User('ryan', 'bully@gmail.com').make_deposit(5000,20000).display_user_balance()




