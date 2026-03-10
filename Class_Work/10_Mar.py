class Bank:
    b_name = 'Hdfc'
    loc = 'Jaipur'
    amount = 0

    def __init__(self,name,id,balance):
        self.name = name
        self.id = id
        self.balance = balance
    
    def deposit(self):
        am = eval(input('Enter amount to deposit :'))
        if(am > 0):
            self.balance += am
            print(f'{am} is deposited successfully')

        else:
            print('Invalid amount to deposit')

    def withdrawl(self):
        am = eval(input('Enter amount to withdraw :'))
        if(am < 0):
            print(f'{am} is invalid amount')
        elif(am <= self.balance):
            self.balance -= am
            print(f'{am} withrawl successfull ')
        else:
            print('Insufficient balance')

    def checkBal(self):
        print(f'Your Balance is {self.balance}')

user1 = Bank('Kartik',101,100)
user1.checkBal()
user1.withdrawl()
user1.deposit()
user1.checkBal()