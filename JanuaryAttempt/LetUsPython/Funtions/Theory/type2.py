# using positional and keyword arguments
def print_it(i, a, str):
    print(i, a, str)

print_it(10, a=3.14, str='Ngp')
print_it(10, str='Ngp', a=3.14)
#print_it(str='Ngp', 10, a=3.14)
#print_it(str='Ngp', a=3.14, 10)