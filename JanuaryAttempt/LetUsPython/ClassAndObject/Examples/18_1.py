'''
Write a class called Number which maintains an integer. It should have
following methods in it to perform various operations on the integer:
set_number(self, n) # sets n into int
get_number(self) # return current value of int
print_number(self) # prints the int
isnegative(self) # checks whether int is negative
isdivisibleby(self, n) # checks whether int is divisible by n
absolute_value(self) # returns absolute value of int
'''

class Number:
    def set_number(self, n):
        self.__num=n
    def get_number(self):
        return self.__num
    def print_number(self):
        print(self.__num)
    def isnegative(self):
        if self.__num < 0:
            return True
        else:
            return False

    def isdivisibleby(self, n):
        if n == 0:
            return False
        if self.__num % n == 0:
            return True
        else:
            return False
        
    def absolute_value(self):
        if self.__num >= 0:
            return self.__num
        else:
            return -1*self.__num

x=Number()
x.set_number(-1234)
x.print_number()
if x.isdivisibleby(5) == True:
    print('5 divides {}'.format(x.get_number()))
else:
    print('% does not divide {}'.format(x.get_number()))

print("Absolute value of {} is {}".format(x.get_number(), x.absolute_value()))