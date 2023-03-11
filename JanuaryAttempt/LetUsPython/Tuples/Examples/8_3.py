'''
A list contains names of boys and girls as its elements. Boys' names are
stored as tuples. Write a Python program to find out number of boys
and girls in the list.
'''

lst = ['Shubha', 'Nisha', 'Sudha', ('Suresh',), ('Rajesh', ), 'Radha']
boys = 0
girls = 0
for ele in lst:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1
print('Boys =', boys, 'Girls = ', girls)