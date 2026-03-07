# GLobal Variable -> which is present in main memory space i.e value space ; It is accessible through out the code
# Local Variable -> which is present in method block i.e inside function ; It can only be accessed inside the function
# gloabl keyword -> the value of variable changed inside function is changed  througout the program


# a = 500
# def fname():
    #global a
#     a = 50
#     b = 100
#     print(a+b)
#     def fun2():
#         nonlocal b
#         b =500
#     fun2()
#     print(b)
# fname()

# print(a)


# Task 1
# li = []
# def prodlist(li):
#     prod = 1
#     for i in li:
#         prod *= i
#     return prod
# print(prodlist(eval(input("Enter a list :"))))


# # Task 2
# name = input("Enter your name :")
# ch = input("Enter charcter to find :")
# def initial(name,ch):
#     for i in  range(len(name)):
#         if(ch == name[i]):
#             return i
#     return "No such character present"
# print(initial(name,ch))


#  Single Packing (Tuple Packing)
# def in_ind(v,*t):
#     for i in range(len(t)):
#         if t[i] == v:
#             print(t)
#             return i
#     return -1
# print(in_ind(100,50,20,30,100,150))


#  Double Packing (Dictionary Packing)
def dou_ind(**d):
    return d
print(dou_ind(a=100,b=20,c=30,d=10))



