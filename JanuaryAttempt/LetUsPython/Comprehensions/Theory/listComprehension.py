import random
# generate 20 rfandom numbers in the range 10 to 100
a = [random.randint(10, 100) for n in range(20)]
print(a)

# generate square and cube of all numbers betweem 0 and 10
a = [(c, c**2, c**3) for c in range(10)]
print(a)

# convert a list oof strings to a list of integers
a = [int(x) for x in ['10', '20', '30', '40']]
print(a)

# using if in list comprehension
# generate a list of even numbers in the range 10 to 30
a = [n for n in range(10, 30) if n % 2 == 0]
print(a)

# form a lisrt deleteall numbers having a value between 20 and 50
a = [num for num in a if num < 20 or num > 50]
print(a)

# when if - else both are used, place tem before or
# replace a vowel in string with !
a = ['!' if alphabet in 'aeiou' else alphabet for alphabet in 'Technical']
print(a)

# using multiple fors and ifs in list comprehension
# flatten a list of lists
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13]]
b=[n for ele in arr for n in ele]

print(b)

# * can be used to unpack a list
c=[*arr[0], *arr[1], *arr[2]]
print(c)

# nested for in a list comprehension and nested comprehension
# produces [4, 5, 6, 5, 6, 7, 6, 7, 8]. uses nested for
lst=[a+b for a in [1, 2, 3] for b in [3, 4, 5]]
print(lst)

# produces [[4, 5, 6], [5, 6, 7],[6, 7, 8]]. uses nested comprehension
lst=[[a+b for a in [1, 2, 3]] for b in [3, 4, 5]]
print(lst)

# use of multiple fors and ifs in list comprehensions
# generate all unique combinations of 1, 2, 3
a=[(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3] if i != j and j != k and k != i] 