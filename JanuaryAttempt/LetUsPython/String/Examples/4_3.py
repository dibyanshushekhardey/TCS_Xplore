'''
For the following strings find out which are having only alphabets, which
are numeric, which are alphanumeric, which are lowercase, which are
uppercase. Also find out whether 'And Quiet Flows The Don' begins with
'And' or ends with 'And' :
'NitiAayog'
'And Quiet Flows The Don'
'1234567890'
'Make $1000 a day
'''

s1='NitiAayog'
s2='And Quiet Flows The Don'
s3='1234567890'
s4='Make $1000 a day'
print('s1 = {}'.format(s1))
print('s2 = {}'.format(s2))
print('s3 = {}'.format(s3))
print('s4 = {}'.format(s4))

# content test functions
print('check isalpha on s1, s2')
print(s1.isalpha())
print(s2.isalpha())

print('check isdigit on s3, s4')
print(s3.isdigit())
print(s4.isdigit())

print('check isalnum on s1, s2, s3, s4')
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())

print('check islower on s1, s2')
print(s1.islower())
print(s2.islower())

print('check isupper on s1, s2')
print(s1.isupper())
print(s2.isupper())

print('check startswith and endswith on s2')
print(s2.startswith('And'))
print(s2.endswith('And'))