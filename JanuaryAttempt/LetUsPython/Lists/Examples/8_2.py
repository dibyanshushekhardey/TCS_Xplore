'''
Perform the following operations on a list of numbers.
- Create a list of 5 odd numbers
- Create a list of 5 even numbers
- Combine the two lists
- Add prime numbers 11, 17, 29 at the beginning of the combined list
- Report how many elements are presentin the list
- Replace last 3 numbersin the list with 100, 200, 300
- Delete all the numbersin the list
- Delete the list
'''

# create a list of 5 odd numbers
a = [1, 3, 5, 7, 9]
print(a)

# create a list of 5 even numbers
b = [2, 4, 6, 8, 10]
print(b)

# combine the two lists
a = a + b
print(a)

# add prime numbers 11, 17, 29 at the beginning of the combined list
a = [11, 17, 29]+a
print(a)

# report how many elements are present in the list
num = len(a)
print(num)

# replace ;ast 3 numbers in the list with 100, 200, 300
a[num-3:num] = [100, 200, 300]
print(a)

# delete all the numbersin the list
a[:] = [ ]
print(a)

# delete the list
del a