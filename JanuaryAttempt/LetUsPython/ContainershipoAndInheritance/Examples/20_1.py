'''
Define a class Shape. Inherit two classes Circle and Rectangle. Check
programmatically the inheritance relationship between the classes.
Create Shape and Circle objects. Report of which classes are these
objects instances of.
'''

class Shape:
    pass
class Rectangle(Shape):
    pass
class Circle(Shape):
    pass

s=Shape()
c=Circle()

print(isinstance(s, Shape))
print(isinstance(s, Rectangle))
print(isinstance(s, Circle))
print(issubclass(Rectangle, Shape))
print(issubclass(Circle, Shape))
