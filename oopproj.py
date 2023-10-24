from bankac import *

Dave =  bankaccount(10000,"Deve")
Dave.getBalance()
Dave.deposit(300)
Dave.withdraw(400)

Sara =  bankaccount(100,"Sara")
Sara.getBalance()
Sara.deposit(400)
Sara.withdraw(1700)

Dave.transfer(10000,Sara)
Dave.transfer(10,Sara)

Jim= InterestRewardsAcc(1000,"Jim")
Jim.getBalance()
Jim.interest(100)

Jim.transfer(90,Dave)

Blaze = SavingsAcct(1000,"Blaze")
Blaze.getBalance()
Blaze.interest(100)
Blaze.transfer(90,Sara)
Blaze.getBalance()
