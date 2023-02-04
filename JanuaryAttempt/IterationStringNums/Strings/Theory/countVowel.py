# read a string from console and print the 
# count of vowels

word = input()

count = 0


for l in word:
    if l.lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)