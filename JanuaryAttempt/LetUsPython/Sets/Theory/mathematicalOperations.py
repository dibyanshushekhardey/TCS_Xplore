# sets
engineers={'Vijay', 'Sanjay', 'Ajay', 'Sujay', 'Dinesh'}
managers={'Aditya', 'Sanjay'}

# union - all people in both categories
print(engineers | managers)

# intersections - who are engineers and mangers
print(engineers & managers )

# difference engineers who are not managers
print(engineers - managers)

# difference - managers who are not engineers
print(managers - engineers)

# symmetric difference - managers who are not engineers
# and engineers who are not managers
print(managers ^ engineers)

a = {1, 2, 3, 4, 5}
b = {2, 4, 5}

print(a >= b)
print(a <= b)