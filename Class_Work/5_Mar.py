# print('* * *',' omveer',sep='@',end=' ^')


# n = eval(input("Enter value :"))
# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end=' ')
#     print()

# Task 1
# row = eval(input("Enter row :"))
# col = eval(input("Enter col :"))
# for i in range(0,row):
#     for j in range(0,col):
#         print('#',end=' ')
#     print()

# for i in range(0,4):
#     for j in range(0,4):
#         if(i == j):
#             print('@',end=' ')
#         else:
#             print('*',end=' ')
#     print()


# Lower Triangle => i > j
# Upper Trianle => i < j
# Primary Diagonal => i==j

#Task 2
# for i in range(0,4):
#     for j in range(0,4):
#         if(i == j):
#             print('*',end=' ')
#         elif(i > j):
#             print('#',end=' ')
#         elif(i < j):
#             print('@',end=' ')
#     print()

#Task 3
# row = eval(input("Enter row :"))
# col = eval(input("Enter col :"))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if(i+j == row+1):
#             print('#',end=' ')
#         elif(i+j > row+1):
#             print('@',end=' ')
#         elif(i+j < row+1):
#             print('*',end=' ')
#     print()


# row = eval(input("Enter row :"))
# col = eval(input("Enter col :"))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if(i+j == row+1):
#             print('#',end=' ')
#         elif(i+j > row+1):
#             if((i+j)%2 == 0):
#                 print('@',end=' ')
#             else:
#                 print(' ',end=' ')
#         elif(i+j < row+1):
#             if((i+j)%2 == 0):
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
         
#     print()

# print(dir(dict()))
# s = '  om'
# print(s.strip())

# l = ['a','d','b']
# print(l.sort())


# ----------------------------------------------------------------------------------------------------------------
# Functions
# a = eval(input("Enter first number :"))
# b = eval(input("Enter second number :"))
# c = 0
# d=0

# # Type 1 -> without return and with arguments
# def mult(a,b):
#     c = a*b
#     print(f"Multiplication of {a} and {b} is {c}")
# mult(a,b)

# # Type 2 -> without return and without arguments
# def product():
#     a = int(input('No.1 :'))
#     b = int(input('No.2 :'))
#     print(a*b)
# product()

# # Type 3 -> with return and without arguments
# def prod():
#     a = int(input())
#     b = int(input())
#     return a*b
# print(prod())

# # Type 4 -> with return and with arguments
# def produ(c,d):
#     c = int(input())
#     d = int(input())
#     c*d
# print(produ(c,d))

# Task 5
# l1 = [-4,-5,-2,-6,-1,1,2,3,4,5]
# l2 = []
# def task():
#     for i in l1:
#         if(i < 0):
#             l2.append(i)
#     return l2
# print(task())

# Task 6
# l1 = eval(input("Enter list :"))
# l2 = []
# def task():
#     for i in l1:
#         if(i < 0):
#             l2.append(i)
#     return l2
# print(task())


# m = 5
# for i in range(1,3):
#     m += 2
# print(m)

n = 10
def change():
    global n
    n = 5
    b = 10
    def f2():
        nonlocal b
        b = 2
    f2()
    print(b)
print(n)
print(change())
print(n)

