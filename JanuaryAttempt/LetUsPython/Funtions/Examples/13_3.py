'''
Write a Python program that accepts a hyphen-separated sequence of
words as input and calls a function convert( ) which converts it into a
hyphen-separated sequence after sorting them alphabetically. For
example, if the input string is
'here-come-the-dots-followed-by-dashes'
then, the converted string should be
'by-come-dashes-dots-followed-here-the'
'''

def convert(s1):
    items=[s for s in s1.split('-')]
    items.sort()
    s2='-'.join(items)
    return s2

s='here-come-the-dots-followed-by-dashes'
t=convert(s)
print(t)