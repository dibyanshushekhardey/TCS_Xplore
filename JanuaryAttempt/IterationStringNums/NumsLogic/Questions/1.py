# WAP to read a word from python and find the number of occurances of vowels
n = input()
count = 0
l = ['a', 'e', 'i', 'o', 'u']
lst = [x for x in n]
for i in lst:
    if i in l:
        count += 1
print(count)