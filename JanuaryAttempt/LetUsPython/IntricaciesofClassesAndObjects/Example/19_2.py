'''
Create a class Date that has a list containing day, month and year
attributes. Define an overloaded == operator to compare two Date
objects.
'''

class Date:
    def __init__(self, d, m, y):
        self.__day, self.__mth, self.__yr=d, m, y
    def __eq__(self, other):
        if self.__day == other.__day and self.__mth == other.__mth and self.__yr == other.__yr:
            return True
        else:
            return False

d1 = Date(17, 11, 98)
d2 = Date(17, 11, 98)
d3 = Date(19, 10, 92)
print(id(d1))
print(id(d2))
print(d1 == d3)