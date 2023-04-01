'''
Create two lists students and marks. Create a dictionary from these two
lists using dictionary comprehension. Use names as keys and marks as
values.
'''
lstnames=['Sunil', 'Sachin', 'Rahul', 'Kapil', 'Rohit']
lstmarks=[54, 65, 45, 67, 78]
d = {k:v for (k, v) in zip(lstnames, lstmarks)}
print(d)