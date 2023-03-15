'''
Paper of size A0 has dimensions 1189 mm x 841 mm. Each subsequent
size A(n) is defined as A(n-1) cut in half, parallel to its shorter sides.
Write a program to calculate and print paper sizes A0, A1, A2, … Aϴ
using recursion.
'''

def papersize(i, n, l, b):
    if n != 0:
        print(f'A{i}: L={int(l)} B = {int(b)}')
        newb = l/2
        newl = b
        n -= 1
        i += 1
        papersize(i, n, newl, newb)

papersize(0, 7, 1189, 841)