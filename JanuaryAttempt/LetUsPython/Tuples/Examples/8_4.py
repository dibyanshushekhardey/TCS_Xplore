'''A list contains tuples containing roll number, names and age of student.
Write a Python program to gather all the names from this list into
another list.
'''

lst = [('A101', 'Shubha', 23), ('A104', 'Nisha', 25), ('A111', 'Sudha', 24)]
nlst = []
for ele in lst:
    nlst += [ele[1]]
print(nlst)