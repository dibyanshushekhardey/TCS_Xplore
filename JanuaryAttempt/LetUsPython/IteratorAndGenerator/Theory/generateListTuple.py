words=['A', 'coddle', 'called', 'Molly']
numbers=[10, 20, 30, 40] 
it=zip(words, numbers)
lst=list(it)
print(lst)

it=zip(words, numbers)
tpl=tuple(it)
print(tpl)

it=zip(words, numbers)
s=set(it)
print(s)