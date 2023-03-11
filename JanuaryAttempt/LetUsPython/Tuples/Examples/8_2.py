'''
Write a Python program to perform the following operations:
- Pack first 10 multiples of 10 into a tuple
- Unpack the tuple into 10 variables, each holding 1 value
- Unpack the tuple such that first value gets stored in variable x, last
value in y and all valuesin between into disposable variables _
- Unpack the tuple such that first value gets stored in variable i, last
value in j and all values in between into a single disposable variable _
'''

tpl = (10, 20, 30, 40,50, 60, 70, 80, 90, 100)
a, b, c, d, e, f, g, h, i, j = tpl
print(tpl)
print(a, b, c, d, e, f, g, h, i, j)
x, _, _, _, _, _, _, _, _, y = tpl
print(x, y, _)
i, *_, j = tpl
print(i, j, _)