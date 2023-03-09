# mutability
animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']
ages = [25, 26, 25, 27, 26, 28, 25]
animals[2] = 'Rhinoceros'
ages[5] = 31
print(animals)
print(ages)

# concatenation
lst = [12, 15, 13, 23, 2, 16, 17]
lst = lst + [33, 44, 55]
print(lst)

# merging 
s = [10, 20, 30]
t = [100, 200, 300]
z = s + t
print(z)

# conversion
l = list('Africa')
print(l)

# aliasing
lst1=[10, 20, 30, 40, 50]
lst2 = lst1
print(lst1)
print(lst2)
lst1[0] = 100
print(lst1[0], lst2[0])


# cloning
lst1 = [10, 20, 30, 40, 50]
lst2 = []
lst2 = lst1 + lst2
print(lst1)
print(lst2)

# searching
lst = ['a', 'e', 'i', 'o', 'u']
res = 'a' in lst
print(res)
res = 'z' not in lst
print(res)

# identity
lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 20, 30, 40, 50]
lst3 = lst1
print(lst1 is lst2)
print(lst1 is lst3)
print(lst1 is not lst2)
 
num1 = 10
num2 = 10
s1 = 'Hi'
s2 = 'Hi'
print(num1 is num2)
print(s1 is s2)

# comparison
a = [1, 2, 3, 4]
b = [1, 2, 5]
print(a < b)

