'''
Write a program that proves that a list is an iterable and not an iterator.
'''
lst=[10, 20, 30, 40, 50]
print(dir(lst))
i=iter(lst)
print(dir(i))