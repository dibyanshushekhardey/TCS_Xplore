from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
class Rectangle(Shape):
    def draw(self):
        print('In Rectangle.draw')

class Circle(Shape):
    def draw(self):
        print('In circle.draw')

#s=Shape()
c=Circle()
c.draw()