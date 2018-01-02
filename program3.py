class Bank(object):

    def __init__(self):
        self.balance=0
    def deposite(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance



chris = Bank()


chris.deposite(100)
chris.withdraw(22)
chrisLoan.makeLoan(200)
print(chris.balance)
print(chrisLoan.loanamount)