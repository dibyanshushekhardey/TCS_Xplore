'''
Given the following tuple
('F', 'l', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
Write a Python program to carry out the following operations:
- Add an ! at the end of the tuple
- Convert a tuple to a string
- Extract ('b', 'b') from the tuple
- Find out number of occurrences of 'e' in the tuple
- Check whether 'r' exists in the tuple
- Convert the tuple to a list
- Delete characters 'b, 'b', 'e', 'r' from the tuple
'''

tpl = ('F', 'l', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
tpl = tpl + ('!',)
print(tpl)

# covert tuple to string
s=''.join(tpl)
print(s)

# extract ('b', 'b') from the tuple
t = tpl[3:5]
print(t)

# coutn number of 'e' in the tuple
count = tpl.count('e')
print('count = {}'.format(count))

# check whether 'r' exists in the tuple
print('r' in tpl)

# covert the tuple to a list
lst = list(tpl)
print(lst)

# tuples are immutable so we cannot remove elemets from a tuple
# there is a need to splt the tuple, eliminate the unwanted elent and them merge the tuples
tpl = tpl[:3] + tpl[7:]
print(tpl)