print((lambda n:n*n*n)(3))
print((lambda x, y, z:(x+y+z)/3)(10, 20, 30))
print((lambda s:s.lstrip().rstrip().upper())('    Ngp'))
p=lambda n:n*n*n
q=lambda x, y, z:(x+y+z)/3
r=lambda s:s.lstrip().rstrip().upper()
print(p(3))
print(q(10, 20, 30))
print(r('   Nagpur   '))

lst1=[1, 2, 3, 4, 5]
lst2=[10, 20, 30, 40, 50]
print((lambda l:sum(l)/len(l))(lst1))
print((lambda l:sum(l)/len(l))(lst2))