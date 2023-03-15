'''
Suppose there are two lists, one containing numbers from 1 to 6, and
other containing umbers from 6 to 1. Write a program to obtain a list
that contains elements obtained by adding corresponding elements of
the two lists.
'''

lst1 = [1, 2, 3, 4, 5, 6]
lst2=[6, 5, 4, 3, 2, 1]
result=map(lambda n1, n2:n1+n2, lst1, lst2)
print(list(result))