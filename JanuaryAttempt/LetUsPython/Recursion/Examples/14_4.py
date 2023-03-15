'''
Write a recursive function to obtain first 15 numbers of a Fibonacci
sequence. In a Fibonacci sequence the sum of two successive terms
gives the third term. First few terms of the Fibonacci sequence:
1 1 2 3 5 8 13 21 34 55 89
'''

def fibo(old, current, terms):
    if terms >= 1:
        new = old + current
        print(f'{new}', end='\t')
        terms = terms - 1
        fibo(current, new, terms)

old = 1
current = 1
print(f'{old}', end='\t')
print(f'{current}', end='\t')
fibo(old, current, 13)