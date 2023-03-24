class Bird:
    pass

b=Bird()

# create attributes dynamically
b.name='Sparrow'
b.weight=500
b.color='light brown'
b.animaltype='Vertebrate'

# modify attributes dynamically
b.weight=450
b.color='brown'

# delete attribues dynamically
del b.animaltype

a=float(25)
b=tuple([10, 20, 30])
c=list('Hello')
d=str([10, 20, 30])

class String:
    def __init__(self, s=''):
        self.__str=s
    def display(self):
        print(self.__str)
    def __init__(self):
        return int(self.__str)

s1=String(123)
s1.display()
i=int(s1)
print(i)