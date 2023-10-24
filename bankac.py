class BalanceException(Exception):
    pass

class bankaccount:
    def __init__(self,initamt,balance):
        self.balance = initamt
        self.name = balance
        print(f"\nAccount '{self.name}' Created.\nBalance= ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance=self.balance+amount
        print("\nDeposit Complete.")
        self.getBalance()
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return amount
        else:
            raise BalanceException(
                f"\nSorry,'{self.name}' Insufficiant Balance. \nyour have ${self.balance:.2f}"
            )
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\n Withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted:{error}")
            
    def transfer(self,amount,account):
        try:
            print('\n*****************\n\nBeginning Transfer.. ')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed\n\n*****************')
        except BalanceException as error:
            print(f"\n Transfer interrupted:{error}")

#inheratance of bankaccount class
class InterestRewardsAcc(bankaccount):
    def interest(self, amount):
        self.deposit(amount)
        self.balance = self.balance+round(amount *5/100,2)
        print('\nInterest Deposit Completed')
        self.getBalance()
        
class SavingsAcct(InterestRewardsAcc):
    def __init__(self,initamt,acctname):  
        super().__init__(initamt,acctname)
        self.fee=5
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount +self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\n withdraw completed")
            self.getBalance()
        except BalanceException as error:
            print(f'\n withdraw intrupted:{error}')  
        
        
        
        
        
        
        
        
        
        
        
