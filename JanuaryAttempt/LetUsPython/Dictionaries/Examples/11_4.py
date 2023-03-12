'''
Write a program to create three dictionaries and concatenate them to
create fourth dictionary.
'''

d1 = {'Mango' : 30, 'Guava': 20}
d2 = {'Apple' : 70, 'Pineapple' : 50}
d3 = {'Kiwi' : 90, 'Banana' : 35}
d4 = {}

for d in (d1, d2, d3):
    d4.update(d)
print(d4)

# one more way
d5={**d1, **d2, **d3}
print(d5)

# will unpack only the keys into the list
d6=list({*d1, *d2, *d3})
print(d6)