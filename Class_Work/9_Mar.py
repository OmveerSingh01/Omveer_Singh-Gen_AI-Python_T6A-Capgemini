# Class is a blueprint of object and objects are instances or real world entities 
class College:
    c_name = 'Jecrc'  # c_name and loc are attributes
    loc = 'Jaipur'
    state = 'Rajasthan'

# Memory Allocation of attributes
# c_name and loc are stored in key layer in value space and their value will be denoted by
#  their address because it is a multivalue datatype so they are stored at other memory block and 
#  the address of key layer is stored in variable space



#Object creation
# Memory Allocation of objects
# A memory block will be created and then the attributes will be defined there and in their value layer , 
# the refernce of these attributes is stored
#  and then the object name will be stored in key layer and itd address stores in valye layer
# s1 = College()
# s1.name = 'Kartik'
# s1.address = 'Pbc'
# s1.age = 22

# s2 = College()
# s2.name = 'Raj'
# s2.address = 'Ajmer'
# s2.age = 25

# s3 = College()
# s3.name = 'Om'
# s3.address = 'Kuchaman'
# s3.age = 20

# print(College)
# print(s1)

# print(s1.name)
# print(s2.name)
# print(s3.name)
# print('')

# print(s1.address)
# print(s2.address)
# print(s3.address)
# print('')

# print(s1.age)
# print(s2.age)
# print(s3.age)
# print('')

# print(s1.c_name)
# print(s1.loc)


# Constructor -> created by __init__ . It is called automatically when class is called 
# Creating constructor
    def __init__(self,name,address,age,marks,state='Rajasthan'):
        self.name = name
        self.address = address
        self.age = age
        self.marks = marks
        self.state = state

    def display(self):                                              #object Method
        self.loc = 'Jodhpur'
        print(self.name,self.address,self.age,self.marks,self.state,self.loc,sep='\n')

        # print(f'Name is {self.name}')
        # print(f'Address is {self.address}')
        # print(f'Age is {self.age}')
        # print(f'Marks is {self.marks}')
        # print(f'State is {self.state}')

    # Class Method
    @classmethod
    def c_disp(cls):
        cls.c_name = 'hgcbg'
        print(cls.c_name, cls.loc, sep='\n')


    @staticmethod
    def add(a,b):
        return a+b
    
print(College.add(10,20))



#s1 is object
s1 = College('Kartik','Pbc',22,90)
s2 = College('harsh','Pbc',22,90)





# s1.c_disp()
# print()
# print(s1.c_name)
# print(s2.c_name)
# s1.display()

# print(s1.loc)
# print(s2.loc)

# s1.c_disp()
# College.c_disp()
