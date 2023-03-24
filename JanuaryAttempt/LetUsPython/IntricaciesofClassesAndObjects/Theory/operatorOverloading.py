class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.__real=r
        self.__imag=i
    
    def __add__(self, other):
        z=Complex()
        z.__real=self.__real+other.__real
        z.__imag=self.__imag+other.__imag
        return z
    
    def __sub__(self, other):
        z=Complex()
        z.__real=self.__real-other.__real
        z.__imag=self.__imag-other.__imag
        return z
    
    def display(self):
        print(self.__real, self.__imag)

c1=Complex(1.1, 0.2)
c2=Complex(1.1, 0.2)
c3=c1+c2
c3.display()
c4=c1-c2
c4.display()