'''
Create 3 listsͶa list of names, a list of ages and a list of salaries.
Generate and print a list of tuples containing name, age and salary from
the 3 lists. From this list generate 3 tuplesͶone containing all names,
another containing all ages and third containing all salaries.
'''

names=['Amol', 'Anil', 'Akash']
ages=[25, 23, 27]
salaries=[34555.50, 40000.00, 450000,00]
it=zip(names, ages, salaries)

lst=list(it)
print(lst)

n, a, s=zip(*lst)
print(n)
print(a)
print(s)