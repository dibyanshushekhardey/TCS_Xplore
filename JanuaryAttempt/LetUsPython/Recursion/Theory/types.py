# head recursiomn
def headprint(n):
    if n == 0:
        return 
    else:
        headprint(n-1)
        print(n)

headprint(10)

# tail recursion
def tailprint(n):
    if n == 11:
        return
    else:
        print(n)
        tailprint(n+1)

tailprint(1)