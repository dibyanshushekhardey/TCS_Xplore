def print_it(a, b, c, d, e):
    print(a,b, c, d, e)

lst=[10, 20, 30, 40 ,50]
tpl=('A', 'B', 'C', 'D', 'E')
s={1, 2, 3, 4, 5}
print_it(*lst)
print_it(*tpl)
print_it(*s)

def another(name='Sanjay', marks=75):
    print(name, marks)
d={'name':'Anil', 'marks':50}
another(*d)
another(**d)