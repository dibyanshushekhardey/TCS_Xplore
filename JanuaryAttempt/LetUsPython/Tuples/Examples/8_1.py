'''
Pass a tuple to the divmod( ) function and obtain the quotient and the
remainder.
'''

result = divmod(17, 3)
print(result)
t = (17, 3)
result = divmod(*t)
print(result)