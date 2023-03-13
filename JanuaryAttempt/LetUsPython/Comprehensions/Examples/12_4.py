'''
Write a program using list comprehension to eliminate empty tuples
from a list of tuples.
'''

lst=[(), (), (10), (10, 20), ('',), (10, 20, 30), (40, 50), (), (45)]
lst=[tpl for tpl in lst if tpl]
print(lst)