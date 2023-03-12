'''
Create a list of cricketers. Use this list to create a dictionary in which the
list values become keys of the dictionary. Set the values of all keys to 50
in the dictionary created
'''

lst=['Sunil', 'Sachin', 'Rahul', 'Kapil', 'Sunil', 'Rahul']
d=dict.fromkeys(lst, 50)
print(len(lst))
print(len(d))
print(d)