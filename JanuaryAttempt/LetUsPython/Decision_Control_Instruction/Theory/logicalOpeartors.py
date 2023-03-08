# and operator
a=40
b=30
x=75 and a >= 20 and b < 60 and 35
z=-30 and a>= 20 and 0 and 35
print(x)
print(z)

# or operator
a=40
b=30
x=75 or a >= 20 or 60
y = a >= 20 or 75 or 60
z = a < 20 or 0 or 35
print(x)
print(y)
print(z)

# not operator
a=10
b=20
not(a <= b)
not(a >= b)

# shortcut for toggling values between 1 and 0
a = input('Enter 0 or 1: ')
a = not a
print(a)