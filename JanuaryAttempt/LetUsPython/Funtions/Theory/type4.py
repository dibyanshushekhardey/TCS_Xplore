def print_it(**kwargs):
    print()
    for name, value in kwargs.items():
        print(name, value, end='')

print_it(a=10)
print_it(a=10, b=3.14)
print_it(a=10, b=3.14, s='Sicilian')
dct={'Student':'Ajay', 'Age':23}
print_it(**dct)