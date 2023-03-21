class Employee:
    def set_data(self, n, a, s):
        self.__name=n
        self.__age=a
        self.__salary=s

    def display_data(self):
        print(self.__name, self.__age, self.__salary)

    def __init__(self, n='', a=0, s=0.0):
        self.__name=n
        self.__age=a
        self.__salary=s

    def __del__(self):
        print('Deleting object'+str(self))

e1=Employee()
e1.set_data('Suresh', 25, 30000)
e1.display_data()
e2=Employee('Ramesh', 23, 25000)
e2.display_data()
e1=None
e2=None