'''
Write a program that defines a function count_alphabets_digits( ) that
accepts a string and calculates the number of alphabets and digits in it. It
should return these values as a dictionary. Call this function for some
sample strings.
'''

def count_alphabets_digits(s):
    d={'Digits':0, 'Alphabets':0}
    for ch in s:
        if ch.isalpha():
            d['Alphabets'] += 1
        elif ch.isdigit():
            d['Digits'] += 1
        else:
            pass
    return d
d = count_alphabets_digits('James Bond 007')
print(d)
d=count_alphabets_digits('Kholi Number 420')
print(d)