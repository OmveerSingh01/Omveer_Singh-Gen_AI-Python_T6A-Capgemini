Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 5
b = 10
c = 25
d = 100
a+a
10
a+a*b+a
60
a+(-a)
0
type(a+float(b))
<class 'float'>
"10"+14
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    "10"+14
TypeError: can only concatenate str (not "int") to str
"hello"+[1,2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    "hello"+[1,2]
TypeError: can only concatenate str (not "list") to str
[1,2]+(1,2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    [1,2]+(1,2)
TypeError: can only concatenate list (not "tuple") to list
"10"-5
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    "10"-5
TypeError: unsupported operand type(s) for -: 'str' and 'int'
10-"5"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    10-"5"
TypeError: unsupported operand type(s) for -: 'int' and 'str'
str(10)-"5"
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str(10)-"5"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
10-5
5
"10"-"5"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    "10"-"5"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
"aksh"-"a"
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    "aksh"-"a"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
{10,20}-{10,1}
{20}
2*{10,20}
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    2*{10,20}
TypeError: unsupported operand type(s) for *: 'int' and 'set'
2*(1,4)
(1, 4, 1, 4)
2*{1,4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
2*[1,4]
[1, 4, 1, 4]
2+2j/2
(2+1j)
3+2j//2
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    3+2j//2
TypeError: unsupported operand type(s) for //: 'complex' and 'int'
(2+2j)/2
(1+1j)
(2+5j)/2
(1+2.5j)
(2+5j)//2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    (2+5j)//2
TypeError: unsupported operand type(s) for //: 'complex' and 'int'
True/True
1.0
[2,3,4,5]/2
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    [2,3,4,5]/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
"10"/2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    "10"/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
5 and 5
5
5 and 4
4
set() and set()
set()
10 and 40
40
5 and 6
6
0.0 and 2.4
0.0
10 && 40
SyntaxError: invalid syntax
0 or 40
40
1 or 2
1
bool(set())
False
bool(' ')
True
bool('')
False
bool(0j)
False
type({})
<class 'dict'>
bool(.)
SyntaxError: invalid syntax
bool(0j and 0j)
False
bool(0j or 0j)
False
bool(1 or 0j)
True
bool(1 and 0j)
False
0 and 2
0
list()
[]
type(list)
<class 'type'>
type(set)
<class 'type'>
not 5
False
not 0
True
not 5 and 0
False'
a+=5
a
10
100 and [] or '' and []
''
5 and 0
0


a=10
a+=a
a
20
a-=a
a
0
a+=5
a
5
a*=5
a
25
a/=5
a
5.0
a//=2
a
2.0
True and [] or not(False) and '',[] or not([]) and False
('', False)
False or 0.0 and 0j or 0
0
a**=2
a
4.0
5>=4
True
5!=5
False
set()==0j
False
1+2j <=0j
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    1+2j <=0j
TypeError: '<=' not supported between instances of 'complex' and 'complex'
1+2j < 0
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    1+2j < 0
TypeError: '<' not supported between instances of 'complex' and 'int'
"a" > "b"
False
"ao" < "ap"
True
1+'a'
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    1+'a'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
ord(a)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    ord(a)
TypeError: ord() expected string of length 1, but float found
ord('a')
97
ord('A')
65
5 in 10
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    5 in 10
TypeError: argument of type 'int' is not a container or iterable
[5] in [10]
False
'ak' < 'kh'
True
ord('H')
72
>>> ord(2)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    ord(2)
TypeError: ord() expected string of length 1, but int found
>>> ord('2')
50
>>> 'hi' > 'his'
False
>>> [10,20] > [20,10]
False
>>> {1,2} > {1}
True
>>> {10} > {1,2}
False
>>> {10,1,2} > {1,2,3}
False
>>> 1.0 == 1
True
>>> True == 1.0
True
>>> True == 1+0j
True
>>> True === 1
SyntaxError: invalid syntax
>>> (1,2) == [1,2]
False
>>> {1,2,4} == {4,1,2}
True
>>> 
>>> {True, 'hi', 2} = {1,2,'hi'}
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
>>> {True, 'hi', 2} == {1,2,'hi'}
True
>>> "hi"*5
'hihihihihi'
>>> "1" == 1
False
>>> [5] in [5,10]
False
>>> 5 in [5,10]
True
>>> bin(100)
'0b1100100'
>>> bin(5)
'0b101'
