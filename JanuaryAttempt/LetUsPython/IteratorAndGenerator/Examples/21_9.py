'''
Create a dictionary containing names of students and marks obtained by
them in three subjects. Write a program to print these names in tabular
form with sorted names as columns and marks in three subjects listed
below each student name as shown below.
Rahul Rakesh Sameer
67 59 58
76 70 86
39 81 78
'''
d = {'Rahul':[67,76,39],'Sameer':[58,86,78],'Rakesh':[59,70,81]}
lst=[(k, *v) for k, v in d.items()]
print(lst)

lst=[(k, *v) for k, v in sorted(d.items())]
print(lst)

for row in zip(*lst):
    print(row)
for row in zip(*lst):
    print(*row, sep='\t')
for row in zip(*((k, *v) for k, v in sorted(d.items( )))):
    print(*row, sep='\t')