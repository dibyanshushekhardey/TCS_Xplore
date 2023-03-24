import math
class Message:
    def display(self, msg):
        print(msg)

def fun():
    print('Everything is an object')

i=45
a=3.14
c=3+2j
city='Nagpur'
lst=[10, 20, 30]
tup=(10, 20, 30, 40)
s={'a', 'e', 'i', 'o', 'u'}
d={'Ajay':30, 'Vijay':35, 'Sujay':36}

print(type(i), id(i))
print(type(a), id(a))
print(type(c), id(c))
print(type(city), id(city))
print(type(lst), id(lst))
print(type(tup), id(tup))
print(type(s), id(s))
print(type(d), id(d))
print(type(fun), id(fun))
print(type(Message), id(Message))
print(type(math), id(math))