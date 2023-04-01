words=['A', 'coddle', 'called', 'Molly']
numbers=[10, 20, 30, 40] 

for ele in zip(words, numbers):
    print(ele[0], ele[1])

for ele in zip(words, numbers):
    print(*ele)

for w, n in zip(words, numbers):
    print(w, n)