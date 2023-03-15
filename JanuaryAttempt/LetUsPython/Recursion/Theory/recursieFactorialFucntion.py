def refact(n):
    if n == 0:
        return 1
    else:
        p = n * refact(n-1)
    return p

num=int(input('Enter any number: '))
fact=refact(num)
print('Factorial value = {}'.format(fact))