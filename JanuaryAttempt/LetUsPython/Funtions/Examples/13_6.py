'''
Write a program that defines a function convert( ) that receives a string
containing a sequence of whitespace separated words and returns a
string after removing all duplicate words and sorting them
alphanumerically.
For example, if the string passed to convert( ) is
s = 'Sakhi was a singer because her mother was a singer, and Sakhi\'s
mother was a singer because her father was a singer'
then, the output should be:
'''

def convert(s):
    words=[word for word in s.split('')]
    return ''.join(sorted(list(set(words))))

s = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn\'t really happy"
t = convert(s)
print(t)
s = "Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because her father was a singer"
t = convert(s)
print(t)