msg = ('Fall', 'In', 'Line')
#msg[0] = 'FALL'
#msg[1:3] = ('Above', 'Mark')

# mutable lists, immutable string - all can belong to tuple
s = ([1, 2, 3, 4], [4, 5], 'Ocelot')
print(s)

# if a tuple contains a list, the list can be modified as list is a mutable object
s = ([1, 2, 3, 4], [10, 20], 'Oynx')
s[1][1] = 45
print(s)

# one more way to change forst item of first list
p = s[1]
p[1] = 100
print(s)
