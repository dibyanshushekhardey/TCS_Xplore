class Base:
    def __init__(self):
        self.i=10
        self._a=3.14
        self.__s='Hello'
    def display(self):
        print(self.i, self._a, self.__s)

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.i=100
        self._a=31.44
        self.__s='Good Morning'
        self.j=20
        self._b=6.28
        self.__ss='Hi'

    def display(self):
        super().display()
        print(self.i, self._a, self.__ss)
        print(self.j, self._b, self.__ss)

bobj=Base()
bobj.display()
print(bobj.i)
print(bobj._a)
print(bobj.__s)

dobj=Derived()
dobj.display()
print(dobj.i)
print(dobj._a)
print(dobj.__s)
