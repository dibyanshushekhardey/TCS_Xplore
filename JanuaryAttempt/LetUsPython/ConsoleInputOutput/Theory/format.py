r, l, b = 1.5678, 10.5, 12.66
name, age, salary = 'Dibyanshu', 30, 53000.55

# print in order by position of variables using empty {}
print('radius = {} length = {} breadth = {}'.format(r, l, b))
print('name = {} age = {} salary = {}'.format(name, age, salary))

# print in any desired order
print('radius = {2} length = {1} breadth = {0}'.format(r, l, b))
print('age={1} salary={2} name={0}'.format(name, age, salary))

# print name in 15 columns salary in 10 coumns
print('name = {0:15} salary = {1:10}'.format(name, salary))

#print radius in 10 columns with 2 digits after dev=cimal point
print('radius = {0:10.2f}'.format(r))