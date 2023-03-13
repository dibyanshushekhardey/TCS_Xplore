'''
Write a program to flatten the following list using list comprehension:
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
'''

mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
a=[num for lst in mat for num in lst]
print(a)