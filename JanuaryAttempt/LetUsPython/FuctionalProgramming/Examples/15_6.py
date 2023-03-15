'''
Suppose a dictionary contain key-value pairs, where key is an alphabet
and value is a number. Write a program that obtains the maximum and
minimum values from the dictionary.
'''

d = {'x' : 500, 'y' : 5874, 'z' : 560}
key_max=max(d.keys(), key=(lambda k:d[k]))
key_min=min(d.keys(), key=(lambda k:d[k]))
print('Maximum Value: ', d[key_max])
print('Minimum Value: ', d[key_min])
