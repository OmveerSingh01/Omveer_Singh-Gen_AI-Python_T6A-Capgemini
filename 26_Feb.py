# a = list(input("Enter a value:"))
# print(a+[1,2])
#print(type(a))

#1. Check if number is a 3-digit number or not take user input.
n = eval(input("Enter a number :"))
if(n >=100 and n <=999):
    print("It is a 3 digit number")
else:
    print("It is not a 3-digit number")

#2. Check if string length is greater than 5.
st = input("Enter a string: ")
if(len(st) > 5):
    print("String is greater than 5")
else:
    print("String is less than 5")

#3.	Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’.
l3 = eval(input("Enter a number :"))
if(l3 == 0):
    print("Zero")
else:
    print("Not zero")

#4. Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
age = eval(input("Enter age: "))
id = input("Enter id: ")
if(age >=18 and id =='valid'):
    print("You are eligible to enter")
else:
    print("Not eligible")

#5.Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’.
num = eval(input("Enter a number: "))
if(num >= 10 and num <=50):
    print("In Range")
else:
    print("Not In Range")

#6.Simple calculator (+ or -) take both number and operator symbol from user.
n1 = eval(input("Enter a number : "))
n2 = eval(input("Enter another number :"))
add =  n1+n2
sub =  n1-n2
print("Addition is ",add)
print("Subtraction is ", sub)

#7.Check if username and password are correct if yes, print ‘Login Successful’.
usr = 'Omveer'
pwd = 1234
user = input("Enter username :")
passw = eval(input("enter password :"))
if (user == usr and passw == pwd):
    print("Login Successful")
else:
    print("Not Successful")

#8.Check if temperature is hot or cold.
temp = eval(input("Enter temperature :"))
if (temp >= 25):
    print("Hot")
else:
    print("Cold")

#9.Check if number is palindrome (basic version) or not. If yes, print ‘Palindrome’ if no, print ‘Not Palindrome’.
no1 = input('Enter a number :')
if (no1[0::-1] == no1):
    print("Palindrome number")
else:
    print("Not a palindrome number")


#10.Check if number is greater than 100.
n1 = eval(input("Enter number :"))
if(n1 >100):
    print("Greater than 100")
else:
    print("Smaller than 100")



