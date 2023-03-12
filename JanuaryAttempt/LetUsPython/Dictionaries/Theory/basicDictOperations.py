courses= { 'CS101' : 'CPP', 'CS102' : 'DS', 'CS201' : 'OOP',
'CS226' : 'DAA', 'CS601' : 'Crypt', 'CS442' : 'Web'}
# add, modify, delete
courses['CS444']='Web Services'
courses['CS201']='OOP using java'
print(courses)
del(courses['CS102'])
print(courses)
del(courses)
print(courses)