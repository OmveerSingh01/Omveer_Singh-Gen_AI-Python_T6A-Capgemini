Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=b=c=d=4
a,b
(4, 4)
type(a)
<class 'int'>
int()
0
float(),str(),bool()
(0.0, '', False)
a=.4
a
0.4
e=6.
type(e)
<class 'float'>
d=.
SyntaxError: invalid syntax
f=.0
f
0.0
g=2+2j
g
(2+2j)
j=1
g
(2+2j)
type(g)
<class 'complex'>
complex()
0j
h=False
h
False
type(h)
<class 'bool'>
'
i=-9
abs(i)
9
abs(i)-(-1)
10
j=2.34567
round(j,2)
2.35
min(1,2,4)
1
max(3,5,4)
5
sum(1,2,4,5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sum(1,2,4,5)
TypeError: sum() takes at most 2 arguments (4 given)
sum([1,2,3,4])
10
h='its my bdy'
h
'its my bdy'
k='its 'today''
SyntaxError: invalid syntax. Is this intended to be part of the string?
l="hello 'what' hello"
l
"hello 'what' hello"
par = ''' dskkmsr msfmg msmfmsmc msmefmm sm
dfskdmvmsefsv "what" fjsffjmjfv
'hi' djfvjvjdjjbd'''
par
' dskkmsr msfmg msmfmsmc msmefmm sm\ndfskdmvmsefsv "what" fjsffjmjfv\n\'hi\' djfvjvjdjjbd'
print(par)
 dskkmsr msfmg msmfmsmc msmefmm sm
dfskdmvmsefsv "what" fjsffjmjfv
'hi' djfvjvjdjjbd
str()
''
print(str())

m="akshay"
len(m)
6
m[1]
'k'
id(m[1])
140712105630424
id(m[5])
140712105631096
id(m)
2588841684512
id[-1]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    id[-1]
TypeError: 'builtin_function_or_method' object is not subscriptable
id(m[1])
140712105630424
m[-1]
'y'
m[6]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    m[6]
IndexError: string index out of range
intro = " My name is Akshay"
intro.index(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    intro.index(a)
TypeError: index() argument 1 must be str, not float
intro.index('a')
5
ind1=intro.index('a')
intro.index('a',ind1+1)
16
z= "Hello this is your Python Class Everyone"
i1 = z.index('y')
i2 = z.indx('y',i1+1)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    i2 = z.indx('y',i1+1)
AttributeError: 'str' object has no attribute 'indx'. Did you mean: 'index'?
i2 = z.index('y',i1+1)
i3 = z.index('y', i2+1)
i1,i2,i3
(14, 20, 36)
in1 = z.index('o')
in2 = z.index('o',in1+1)
in3 = z.index('o',in2+1)
in4 = z.index('o',in3+1)
in1,in2,in3,in4
(4, 15, 23, 37)
z.count('o')
4
z.count('o','a')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    z.count('o','a')
TypeError: slice indices must be integers or None or have an __index__ method
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
a="akshay"
a=a+"i"
a
'akshayi'
a[-4]
'h'
address= "15-A Devraj Nagar, Sanganer, Jaipur"
len(address)
35
address[len(address)/2]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    address[len(address)/2]
TypeError: string indices must be integers, not 'float'
l=len(address/2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    l=len(address/2)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
address[35/2]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    address[35/2]
TypeError: string indices must be integers, not 'float'
adress[35/2.]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    adress[35/2.]
NameError: name 'adress' is not defined. Did you mean: 'address'?
address[len(address)//2]
','
list1 = [1,2,3,4]
type(list)
<class 'type'>
type(list1)
<class 'list'>
list()
[]
l1 = ["akshay", "cse25", 21, "21-APR"]
l1[1]
'cse25'
l1[1] = Cs25
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    l1[1] = Cs25
NameError: name 'Cs25' is not defined
l1[1] = "Cs25"
l1
['akshay', 'Cs25', 21, '21-APR']
l3 = [100,200,"hello"]
l3[2][1]
'e'
l1.
SyntaxError: invalid syntax
l1.append('you')
l1.insert(558)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    l1.insert(558)
TypeError: insert expected 2 arguments, got 1
l1
['akshay', 'Cs25', 21, '21-APR', 'you']
l1.append("TRK")
l1.insert(0,1)
l1
[1, 'akshay', 'Cs25', 21, '21-APR', 'you', 'TRK']
l1.insert(8,"SK")
l1
[1, 'akshay', 'Cs25', 21, '21-APR', 'you', 'TRK', 'SK']
l1[8]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    l1[8]
IndexError: list index out of range
l1[7]
'SK'
l1.pop(0)
1
l1
['akshay', 'Cs25', 21, '21-APR', 'you', 'TRK', 'SK']
l1.pop()
'SK'
l1
['akshay', 'Cs25', 21, '21-APR', 'you', 'TRK']
l1.remove("TRK")
l1
['akshay', 'Cs25', 21, '21-APR', 'you']
dir.list()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    dir.list()
AttributeError: 'builtin_function_or_method' object has no attribute 'list'
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
l1.index(21,-1)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    l1.index(21,-1)
ValueError: list.index(x): x not in list
l1.index(21,1)
2
lst = ["Python is Not Easy"]
lst[0][-4]
'E'
lst[-1][-4]
'E'
lst[0][-8]
'N'
lst.count('o')
0
lst[0].count('o')
2
t=(1,2,3,'','hi',False)
type(t)
<class 'tuple'>
tpl=1,2,3,4,''
tpl
(1, 2, 3, 4, '')
tpye(tpl)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    tpye(tpl)
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
type(tpl)
<class 'tuple'>
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
tuple()
()
tpye(lst)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    tpye(lst)
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
type(lst)
<class 'list'>
tx = (1)
type(tx)
<class 'int'>
tx(1,)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    tx(1,)
TypeError: 'int' object is not callable
tx = (1,)
type(tx)
<class 'tuple'>
t1="akshay",21,"jaipur","cse25"
t1
('akshay', 21, 'jaipur', 'cse25')
t1(1)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    t1(1)
TypeError: 'tuple' object is not callable
t1[1]
21
t1[0].count('a')
2
s={1,1,1,1}
s
{1}
s={1,2,[1,2]}
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    s={1,2,[1,2]}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s={1,1.5,1+2j,'hi'}
s
{'hi', 1.5, 1, (1+2j)}
s.add('9')
s
{1.5, 1, (1+2j), '9', 'hi'}
s
{1.5, 1, (1+2j), '9', 'hi'}
type(s)
<class 'set'>
set()
set()
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s.pop()
1.5
>>> s
{1, (1+2j), '9', 'hi'}
>>> s.add(1.5)
>>> s
{1.5, 1, (1+2j), '9', 'hi'}
>>> s
{1.5, 1, (1+2j), '9', 'hi'}
>>> s
{1.5, 1, (1+2j), '9', 'hi'}
>>> s.pop()
1
>>> s.remove(9)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    s.remove(9)
KeyError: 9
>>> s.remove('9')
>>> s
{1.5, (1+2j), 'hi'}
>>> dic1 = {}
>>> dic1
{}
>>> type(dic1)
<class 'dict'>
>>>     dic2 = {name:"akshay",age:21}
...     
SyntaxError: unexpected indent
>>> dic2 = {name:"akshay",age:21}
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    dic2 = {name:"akshay",age:21}
NameError: name 'name' is not defined
>>> dic2 = {"name":"akshay","age":21}
>>> dic2
{'name': 'akshay', 'age': 21}
>>> type(dic2)
<class 'dict'>
>>> dict()
{}
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
