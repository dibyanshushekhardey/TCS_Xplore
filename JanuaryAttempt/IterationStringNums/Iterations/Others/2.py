# check teh anagram in python
str1 = input()
str2 = input()

list1 = list(str1)
list2 = list(str2)

list1.sort()
list2.sort()

if list1 == list2:
    print("{} == {} is true".format(str1, str2))
else:
    print("{} == {} is false".format(str1, str2))