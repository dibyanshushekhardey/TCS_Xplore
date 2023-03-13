'''
Given a string, split it on whitespace, capitalize each element of the
resulting list and join them back into a string. Your implementation
should use a list comprehension.
'''

s1='dreams maty change, but friends are forever'
s2=[''.join(w.capitalize() for w in s1.split())]
s3=s2[0]
print(s3)