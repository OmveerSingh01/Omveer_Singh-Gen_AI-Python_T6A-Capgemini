class Credit_card:
    def pay(self,amount):
        print(f'Rs {amount} paid by credit card')
class UPI:
    def pay(self,amount):
        print(f'Rs {amount} paid by  UPI')
class Cash:
    def pay(self,amount):
        print(f'Rs {amount} paid by cash')

pmt = [Credit_card(),UPI(),Cash()]
for i in pmt:
    i.pay(300)


class Circle:
   

    def __init__(self, ):
         self.rad = rad
        
    def area(self):
        print(f'Area is {3.14*self.rad * self.rad}')
        # self.rad = rad
    
    def perameter(self):
        print(f'Parameter is {2 * 3.14 * self.rad}')
        # self.rad = rad
    
o1 = Circle()
o1.area()
o1.perameter()