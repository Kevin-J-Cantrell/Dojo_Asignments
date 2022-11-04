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
    
saving.deposit(500).deposit(200).deposit(50).withdraw(600).yield_interest().display_account_info()
checking.deposit(500).deposit(500).withdraw(60).withdraw(200).withdraw(100).withdraw(50).yield_interest().display_account_info()
BankAccount.all_acnt()