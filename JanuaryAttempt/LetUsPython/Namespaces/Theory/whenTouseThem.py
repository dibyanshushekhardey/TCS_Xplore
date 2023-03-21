a=20
b=3.14
s='Aabra ka daabra'
lst=['a', 'b', 's']
for var in lst:
    print(globals()[var])

def fun1():
    print('Inside fun1')
def fun2():
    print('Inside fun2')
def fun3():
    print('Inside fun3')

lst=['fun1', 'fun2', 'fun3']
for var in lst:
    globals()[var]()