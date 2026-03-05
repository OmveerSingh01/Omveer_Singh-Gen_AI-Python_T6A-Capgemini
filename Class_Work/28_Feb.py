
# s1 = 'Kartik@Raj@123'
# print(s1.split('@'))

# Task 1
# l1 = ['p1.py', 'first.txt','T3.py' ,'Tk.txt','TFK.com']
# d2 = {}
# for i in l1:
#     j = i.split('.')
#     out = j[1]
#     inn = j[0]

#     if out not in d2:
#         d2[out] = []
#     d2[out].append(inn)
# print(d2)
    

# a = 'aaabbaabcc'
# out = ''
# count = 1
# for i in range(len(a)):
#     if i<len(a)-1 and a[i] == a[i+1]:
#         count += 1
#     else:
#         out += a[i]+ str(count)
#         count =1
# print(out)
    

# l = ['Kartik','Raj','Prince']
# v =''
# for i in l:
#     for j in i:
#         if j in 'aeiouAEIOU':
#             v += j

# print(v)

# inp = [(2+3j),12,'Program','Python',False]
# d = {}
# cd =''
# for i in inp:
#     if(type(i) == str):
#         for j in i:
#             if j in 'aeiouAEIOU':
#                 cd += j
#                 d[i] = cd
#                 # d[i].append(cd)
#         cd=''
# print(d)


#PASS STATEMENT
for i in range(1,11):
    
    if i == 11:
        pass
    else:
        print(i)

