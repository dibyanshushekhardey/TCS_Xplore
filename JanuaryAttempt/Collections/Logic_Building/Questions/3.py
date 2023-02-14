# WAP to read a list from input
# print the subset array of all the odd numbers in the list

n = int(input())

l = []

for i in range(n):
    l.append(int(input()))

list_of_odds = []

for element in l:
    if element % 2 != 0:
        list_of_odds.append(element)

print(list_of_odds)

