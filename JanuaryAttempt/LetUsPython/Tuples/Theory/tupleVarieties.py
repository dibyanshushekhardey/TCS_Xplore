a = (1, 3, 5, 7, 9)
b = (2, 4, 6, 8, 10)
c = (a, b)
print(c[0][0], c[1][2])
print(c)

# creating tuples of tuples
records = (
    ('Priyanka', 24, 3455.5), ('Shailesh', 25, 4555.5),
    ('Subhash', 25, 4505.5), ('Sugandh', 27, 4455.55)
)

print(records[0][0], records[0][1], records[0][2])
print(records[1][0], records[1][1], records[1][2])
for n, a, s, in records:
    print(n, a, s)

# tuple embedded in another tuple
x = (1, 2, 3, 4)
y = (10, 20, *x, 30)
print(y)

# possibility to cretae a list of tuples or a tuple of lists
lst = [('Priyanka', 24, 3455.5), ('Shailesh', 25, 4555.5)]
tpl = (['Priyanka', 24, 3455.5], ['Shailesh', 25, 4555.5])
print(lst)
print(tpl)

# sorting a list of tuples or tuple of lists
import operator
# each embedded tuple/list contains name, age, salary
lst = [('Shailesh', 25, 4555.5), ('Priyanka', 24, 3455.5)]
tpl = (['Shailesh', 25, 4555.5], ['Priyanka', 24, 3455.5])
print(sorted(lst))
print(sorted(tpl))
sorted(lst, key=operator.itemgetter(2))
sorted(tpl, key=operator.itemgetter(2))
