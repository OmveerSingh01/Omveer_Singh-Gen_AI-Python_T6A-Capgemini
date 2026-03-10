file = open('temp.txt','w+')
file.write('I am highest in the room \n')
file.writelines(
    [ 
    'first line \n' 
    'second line \n'
    'third line \n'
    'fourth line \n'
    ]
)
# to make py interpreter to point at a specific index, we use seek
file.seek(0) 
print(file.read())

file.close()