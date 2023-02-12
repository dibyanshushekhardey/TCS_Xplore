# WAP to read a word and a letter from console
# print the word after deleting all the occurences of the letter

a, b = input().split(' ')

c = a.replace(b,"")
print(c)