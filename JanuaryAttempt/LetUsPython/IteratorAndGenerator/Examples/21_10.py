'''
Write a program that defines a function pascal_triangle( ) that displays a
Pascal Triangle of level received as parameter to the function. A Pascal's
Triangle of level 5 is shown below.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''

def pascal_triangle(n):
    row=[1]
    z=[0]
    for x in range(n):
        print(row)
        row=[l+r for l, r in zip(row+z, z+row)]
    
pascal_triangle(5)