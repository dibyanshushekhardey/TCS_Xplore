def print_it(*args):
    print()
    for var in args:
        print(var, end='')

print_it(10)
print_it(10,3.14)
print_it(10,3.14,'Sicilian')
print_it(10, 3.14, 'Sicilian', 'Punekar')