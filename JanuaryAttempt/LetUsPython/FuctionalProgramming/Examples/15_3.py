'''
Write a program to create a new list by obtaining square of all numbers
in a list.
'''

lst1=[5, 7, 9, -3, 4, 2, 6]
lst2=list(map(lambda n:n**2, lst1))
print(lst2)