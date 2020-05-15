'''

For this challenge, create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''
class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: {self.balance}'

    def deposit(self,deposit):
        self.balance += deposit
        return 'Deposit Accepted'
    def withdraw(self,amount):
        if amount > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance -= amount
            print('Withdrawal Accepted')

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

# 6 Make an acceptable withdrawal 
acct1.withdraw(75)

# 7. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
