# creating nested list
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = [a, b]
print(c[0][0], c[1][2])

# list embedded in another list
x = [1, 2, 3, 4]
y = [10, 20, x, 30]
print(y)

# unpack a string or list within a list
s = 'Hello'
l = [*s]
print(l)

x = [1, 2, 3, 4]
y = [10, 20, *x, 30]
print(y)