'''
Write a python code to print the count of valid strings 
and invalid strings from a given list of strings

A string is considered as valid if it contains combinations
of alphabetes (in upper case or lower case) with/without 
spaces.

Define a function to check if a given string is valid or not
i.e if it contains combination of alphabetes.

This function will take string as input and return True 
if the string is valid, otherwise will return False.

Example:

Input:
4
HelloGood Morning
abcd123Fghy
India
Progoto.c

Output:
Count Of Valid String = 2
Count of Invalid String = 2
'''

def validString(l):
    #pass
    countvalid = 0
    countinvalid=0
    for str in l:
        temp = ''
        for word in str.split():
            temp += word.strip()
        if temp.isalpha():
            countvalid += 1
        else:
            countinvalid += 1
    return [countvalid, countinvalid]

n=int(input())
l = []
for i in range(n):
    a=input()
    l.append(a)
valid, invalid = validString(l)
print('Count of valid string = ', valid)
print('Count of invalid string = ', invalid)