# public access specifiers
class employee:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal

e1=employee("Kiran", 100000)
print(e1.salary)
e1.salary=200000
print(e1.salary)

# protected sample - No use
class employee1:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal

e2 = employee1("Kiran", 10000)
print(e2.salary)
e2._salary=20000
print(e2._salary)

# private sample - still not much secured
class employee2:
    def __init__(self, name, sal):
        self.__name=name
        self.__salary=sal

# this wat of private variable variable acess would not work
#e3 = employee2("Kiran", 10000)
#print(e3.__salary)
#e3.__salary=20000
#print(e3.__salary)

# contradicting instruction  -this way we can access private variable stil
e3=employee2("Kiran", 10000)
e3._employee2__salary=22222
print(e3._employee2__salary)