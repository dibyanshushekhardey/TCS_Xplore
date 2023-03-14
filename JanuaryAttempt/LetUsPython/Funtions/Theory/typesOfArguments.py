# positional arguments
def fun(i, j, k):
    print(i+j)
    print(k.upper())

fun(10, 3.14, 'Rigmarole')
# fun('Rigmarole', 3.14, 10)

# keyword arguments
def print_it(i, a, str):
    print(i, a, str)

print_it(a=3.14, i=10, str='Silican')
print_it(str='Sicilian', a=3.14, i=10)
print_it(str='Sicilian', i=10, a=3.14)
#print_it(s='Sicilian', j=10, a=3.14)
