import json
lst=[10, 20, 30, 40, 50, 60, 70, 80, 90]
tpl=('Ajay', 23, 2455.55)
dct={'Anil':24, 'Ajay':23, 'Nisha':22}

str1=json.dumps(lst)
str2=json.dumps(tpl)
str3=json.dumps(dct)
l=json.loads(str1)
t=tuple(json.loads(str2))
d=json.loads(str3)
print(l)
print(t)
print(d)