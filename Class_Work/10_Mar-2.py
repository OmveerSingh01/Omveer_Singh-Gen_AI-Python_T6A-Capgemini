# class Car:
#     wheels = 5
#     engine = 1
#     def start(self):
#         print('Welcome to my car')
# class Kia(Car):
#     def disp(self):
#         print('Kia Seltos - Wild By design')
# o1 = Kia()
# o1.start()
# print(o1.wheels)

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def disp(self):
        print(self.name,self.salary)

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    @property
    def disp1(self):
        print(self.name,self.salary,self.department)

user1 = Manager('Akshay',50000,'IT')
print(user1.name)
print(user1.salary)
print(user1.department)
print()
user1.disp1

        

