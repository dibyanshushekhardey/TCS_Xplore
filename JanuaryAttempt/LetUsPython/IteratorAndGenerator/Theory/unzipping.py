words=['A', 'coddle', 'called', 'Molly']
numbers=[10, 20, 30, 40]
it=zip(words, numbers)
lst=list(it)
w, n=zip(*lst)
print(w)
print(n)