class bankAccout:
    def __init__(self,accountNo):
        self.__balance=0
        self.accountNo=accountNo
    def Balance(self):
        print(self.__balance)
    def deposit(self,amount):
        self.__balance=self.__balance+amount 
    def withdraw(self,amt):
        if self.__balance<amt:
            print("Balance insufficient")
        else:
            self.__balance=self.__balance-amt 
b1=bankAccout(1023)
b1.deposit(1000)
b1.withdraw(600)
b1.withdraw(500000)

    