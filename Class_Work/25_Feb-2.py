Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = "10.5"
float(s)
10.5
int(s)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '10.5'
str([22,23])
'[22, 23]'
l=[('hi','false'),(True,False)]
set(l)
{('hi', 'false'), (True, False)}
[1,2]+1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    [1,2]+1
TypeError: can only concatenate list (not "int") to list
[1,2]+[1]
[1, 2, 1]
l = [10,20,30]
l2 = l
id(l),id(l2)
(2835856388672, 2835856388672)
l2[1] = 200
l2
[10, 200, 30]
id(l2)
2835856388672
l
[10, 200, 30]
ls = [10,20,30]
ls2 = ls.copy()
>>> ls2[1] = 200
>>> ls
[10, 20, 30]
>>> ls2
[10, 200, 30]
>>> ls[3] = [1,2,3]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ls[3] = [1,2,3]
IndexError: list assignment index out of range
>>> ls+[1,2,3]
[10, 20, 30, 1, 2, 3]
>>> ls[3] = [1,2,3]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ls[3] = [1,2,3]
IndexError: list assignment index out of range
>>> ls
[10, 20, 30]
>>> ls.append([1,2])
>>> ls
[10, 20, 30, [1, 2]]
>>> ls3 = ls.copy()
>>> ls
[10, 20, 30, [1, 2]]
>>> ls3
[10, 20, 30, [1, 2]]
>>> ls3[3][1] = 5
>>> ls
[10, 20, 30, [1, 5]]
>>> ls3
[10, 20, 30, [1, 5]]
>>> ls[3].append([100,200])
>>> ls
[10, 20, 30, [1, 5, [100, 200]]]
>>> ls4 = ls.copy()
>>> ls4[3][2][1] = 500
>>> ls
[10, 20, 30, [1, 5, [100, 500]]]
>>> ls4
[10, 20, 30, [1, 5, [100, 500]]]
>>> lst = [10,20,[100,200]]
>>> import copy
>>> lst2 = copy.deepcopy(lst)
>>> lst2[2][0] = 500
>>> lst,lst2
([10, 20, [100, 200]], [10, 20, [500, 200]])
