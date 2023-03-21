'''
Write a program to create a class called Fruit with attributes size and
color. Create multiple objects of this class. Report how many objects
have been created from the class.
'''

class Fruit:
    count = 0
    def __init__(self, name='', size=0, color=''):
        self.__name=name
        self.__size=size
        self.__color=color
        Fruit.count += 1

    def display():
        print(Fruit.count)

f1=Fruit('Banana', 5, 'Yellow')
f2=Fruit('Orange', 4, 'Orange')
f3=Fruit('Apple', 3, 'Red')
Fruit.display()
print(Fruit.count)