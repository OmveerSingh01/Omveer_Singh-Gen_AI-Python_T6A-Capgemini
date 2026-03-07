# Positional Arguments -> The arguments which we pass when declaring a function and then we pass its value in calling
# Default Argument -> The argument which we pass during declaration with its value 
# Keyword Argument -> The argument which we pass during calling with its value 
# def form(name,ph,subject,age = 25,*abc,alt_ph=None):
#     print('Name is',name)
#     print('Phone number is',ph)
#     print('Subject is',subject)
#     print('Age is',age)
#     print('alternate ph',alt_ph)
# form(input('Enter name :'),eval(input('Enter phone :')),input('Enter subject :'),eval(input("Enter value in tuple"),alt_ph=(input('Enter alternate phone no, :'))))

# sys.setrecursionlimit -> It is used toset limit
# import sys
# sys.setrecursionlimit(1030)


# def fact(n):
#     if(n==0) or (n==1):
#         return 1
#     return n*fact(n-1)
# print(fact(int(input('Enter number :'))))

# Task 1
# def Addgs(*a):
#     if(len(a) >= 2 and len(a) <= 5):
#         ans = sum(a)
#         return ans
#     else:
#         return 'Limit exceeded'
#   print(Addgs(*eval(input('Enter numbers :'))))
    
# Task 1 Alternate method
# def alternate(s):
#     if(len(s) >= 2 and len(s) <=5):
#         tot = sum(s)
#         return tot
#     else:
#         return 'Invalid Limit'
# print(alternate(eval(input('Enter numbers :'))))


# Task 2
# def indSum(n):
#     ans =0
#     while(n >0):
#         t = n%10
#         ans += t
#         n //= 10
#     return ans
     
# print(indSum(int(input('Enter a number :'))))

