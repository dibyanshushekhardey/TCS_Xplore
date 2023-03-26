'''
Write a program that defines an abstract class called Printer containing
an abstract method print( ). Derive from it two classes—LaserPrinter
and Inkjetprinter. Create objects of derived classes and call the print( )
method using these objects, passing to it the name of the file to be
printed. In the print( ) method simply print the filename and the class
name to which print( ) belongs.
'''

from abc import ABC, abstractmethod
class Printer(ABC):
    def __init__(self, n):
        self.__name=n
    @abstractmethod
    def print(self, docName):
        pass

class LaserPrinter(Printer):
    def __init__(self, n):
        super().__init__(n)
    def print(self, docName):
        print('>>LaserPrinter.print')
        print('Trying to print: ', docName)

class InkjetPrinter(Printer):
    def __init__(self, n):
        super().__init__(n)

    def print(self, docName):
        print('>>InkjetPrinter.print')
        print('Trying to print: ', docName)

p=LaserPrinter('LaserJet 1100')
p.print('hello1.pdf')
p=InkjetPrinter('IBM 2140')
p.print('hello2.doc')