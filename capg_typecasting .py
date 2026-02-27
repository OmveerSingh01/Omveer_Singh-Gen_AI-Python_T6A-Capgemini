Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = [10,2j,"python",[2+5j,11,22.22]]
b = "python is hard as well as easy"
l = ["python", "is", "Not", "easy"]
a[2],a[-4],b[18],b[-12],l[2][0],l[-2][-3]
('python', 10, 'w', 'w', 'N', 'N')
s1 = "Omveersingh"
s1[3:7:1]
'hayk'
s1[0:1]
'a'
s[9:13]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[9:13]
NameError: name 's' is not defined. Did you mean: 's1'?
s1[9:13]
'tri'
s1[9:13:1]
'tri'
s1[8:14]
'atri'
s1[8:14:-1]
''
s1[8:13:-1]
''
s1[5::-1]
'yahska'
s1[::2]
'asakar'
s1[10:6:-1]
'rtah'
s1[-6:13:1]
'khatri'
s1[6:12:1]
'khatri'
s1[-6::1]
'khatri'
t=(1,2,[23,'hi'],'ok')
t[2]
[23, 'hi']
t[2][0]=25
t
(1, 2, [25, 'hi'], 'ok')
a=5
flaot(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    flaot(a)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
float(a)
5.0
a
5
float(int(a))
5.0
a
5
b=float(a)
b
5.0
c=str(a)
c
'5'
d=list(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d=list(a)
TypeError: 'int' object is not iterable
type(b) , type(c)
(<class 'float'>, <class 'str'>)
a1 = True
b1=list(a1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b1=list(a1)
TypeError: 'bool' object is not iterable
l = [1,2]
a = int(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a = int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a=5
b=bool(a)
set()
set()
dict()
{}
a=1.5
b=int(a)
b
1
str(a)
'1.5'
bool(a)
True
complex(a)
(1.5+0j)
c=1+5j
int(c)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
flaot(c)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    flaot(c)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
bool(c)
True
str(c)
'(1+5j)'
print(str(c))
(1+5j)
b=False
int(b)
0
float(b)
0.0
str(b)
'False'
complex(b)
0j
bool()
False
s="akshay"
int(s)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'akshay'
bool(s)
True
list(s)
['a', 'k', 's', 'h', 'a', 'y']
tuple(s)
('a', 'k', 's', 'h', 'a', 'y')
dict(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
set(s)
{'s', 'a', 'k', 'y', 'h'}
s1="12"
int(s1)
12
flaot(s1)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    flaot(s1)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
float(int(s1))
12.0
complex(s1)
(12+0j)
l = ["po",[1,2],'to']
dict(l)
{'p': 'o', 1: 2, 't': 'o'}
l1 = ("hi",{True,False},(1,),[1,[1,2]])
dict(l1)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    dict(l1)
ValueError: dictionary update sequence element #2 has length 1; 2 is required
>>> l1 = ("hi",{True,False},(1,6),[1,[1,2]])
>>> dict(l1)
{'h': 'i', False: True, 1: [1, 2]}
>>>  s = {1,3,2,'hi',"hi",4,1.56,True,False}
...  
SyntaxError: unexpected indent
>>> s = {1,3,2,'hi',"hi",4,1.56,True,False}
>>> list(s)
[False, 1.56, 2, 1, 3, 4, 'hi']
>>> tuple(s)
(False, 1.56, 2, 1, 3, 4, 'hi')
>>> s
{False, 1.56, 2, 1, 3, 4, 'hi'}
>>> set(l1)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    set(l1)
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
>>> list(tuple(s))
[False, 1.56, 2, 1, 3, 4, 'hi']
>>> l2 = [True,False,0,1,2,3,"hi","45",45]
>>> set(l2),tuple(l2)
({False, True, 2, 3, 'hi', 45, '45'}, (True, False, 0, 1, 2, 3, 'hi', '45', 45))
>>> d = {"name":"akshay", "age":21,"DOB":"21APR"}
>>> d
{'name': 'akshay', 'age': 21, 'DOB': '21APR'}
>>> bool(d)
True
>>> list(d)
['name', 'age', 'DOB']
>>> tuple(d)
('name', 'age', 'DOB')
>>> set(d)
{'age', 'name', 'DOB'}
>>> list(d.items())
[('name', 'akshay'), ('age', 21), ('DOB', '21APR')]
>>> list(d.values())
['akshay', 21, '21APR']
>>> c = list(d.values())
>>> c
['akshay', 21, '21APR']
>>> a = c
>>> a
['akshay', 21, '21APR']
