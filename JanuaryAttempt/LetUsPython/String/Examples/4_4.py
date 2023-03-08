'''
Given the following string:
'Bring It On'
' Flanked by spaces on either side '
'C:\\Users\\Kanetkar\\Documents'
write a program to produce the following output using appropriate
string functions.
BRING IT ON
bring it on
Bring it on
Bring It On
bRING iT oN
6
9
Bring Him On
Flanked by spaces on either side
Flanked by spaces on either side
['C:', 'Users', 'Kanetkar', 'Documents']
('C:', '\\', 'Users\\Kanetkar\\Documents')
'''

s1='Bring It On'
# conversions
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())

# search and replace
print(s1.find('l'))
print(s1.find('On'))
print(s1.replace('It', 'Him'))

# trimming
s2='    Flanked by spaces on either side    '
print(s2.lstrip())
print(s2.rstrip())

# splitting
s3='C:\\Users\\Kanetkar\\Documents'
print(s3.split('\\'))
print(s3.partition('\\'))