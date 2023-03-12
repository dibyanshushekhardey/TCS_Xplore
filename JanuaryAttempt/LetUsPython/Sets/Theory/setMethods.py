s={12, 15,13, 23, 22, 16, 17}
t = {'A', 'B', 'C'}
u=set()
s.add('Hello')
s.update(t)
u=s.copy()
#s.remove(101)
s.discard(12)
s.discard(101)
s.clear()
print(s)
print(t)
print(u)
s={12, 15,13, 23, 22, 16, 17}
t = {13, 15, 22}

print(s.issuperset(t))
print(s.issubset(t))
print(s.isdisjoint(t))