'''
Write a program to receive radius of a circle, and length and breadth of
a rectangle in one call to input( ). Calculate and print the circumference
of circle and perimeter of rectangle
'''

r, l, b = input('Enter radius, length and breath: ').split()
radius = int(r)
length = int(l)
breadth = int(b)
circumference = 2 * 3.14 * radius
perimeter = 2 * (length + breadth)
print(circumference)
print(perimeter)

