'''
Write a program to obtain transpose of a 3 x 4 matrix.
'''

mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9,10, 11, 12]]
ti=zip(*mat)
lst=[[] for i in range(4)]
i = 0
for t in ti:
    lst[i] = list(t)
    i += 1
print(lst)