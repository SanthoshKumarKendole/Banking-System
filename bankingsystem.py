class bank():
    def __init__(self,name,age,mobileno,accno,pin,bal):
        self.name=name
        self.age=age
        self.mobileno=mobileno
        self.accno=accno
        self.pin=pin
        self.bal=bal
    
    def checkbalance(self):
        if self.pin==self.getpin():
            print(f'The current Balance is :{self.bal}')
        else:
            print("Invalid Pin")

    def deposite(self):
        if self.pin==self.getpin():
            amt=int(input("Enter a amount to be deposite: "))
            self.bal+=amt
            print('Amount deposite successfully')
            print(f"The current balance is :{self.bal}")
        else:
            print("Invalid Pin or Trancsaction Failed")
    
    def withdraw(self):
        if self.pin==self.getpin():
            amt=int(input('Enter a amount to be a withdraw: '))
            if self.bal>=amt:
                self.bal-=amt
                print("Amount withdraw Successful")
                print(f'the current balance is {self.bal}')
            else:
                print("Transaction failed")
        else:
            print("Invalid Pin")
    @staticmethod
    def getpin():
        return int(input("Enter a pin : "))
    
obj=bank('Santhosh',23,9490822478,8378432902,1234,10000)
obj.checkbalance()
obj.withdraw()
obj.deposite()