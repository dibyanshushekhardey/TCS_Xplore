'''
Define an abstract class called Character containing an abstract method
patriotism( ). Define a class Actor containing a method style( ). Define a
class Person derived from Character and Actor. Implement the method
patriotism( ) in it, and override the method style( ) in it. Also define a
new method do_acting( ) in it. Create an object of Person class and call
the three methods in it.
'''

from abc import ABC, abstractmethod
class Character(ABC):
    @abstractmethod
    def patriotism(self):
        pass
class Actor:
    def style(self):
        print('>>Actor.Style:')

class Person(Actor, Character):
    def do_acting(self):
        print('>>Person.doActing')

    def style(self):
        print('>>Person.style')
    def patriotism(self):
        print('>>Person.patriotism')

p=Person()
p.patriotism()
p.style()
p.do_acting()