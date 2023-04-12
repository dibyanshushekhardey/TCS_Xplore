'''
Write a python code to print the position or index of a given string(taken as an input from user) from a given list of strings.

The program will take an input from user in the form of a string and will pass the string as argument to a function. The function will take the string as argument and return position(or index) of the list if the passed string is present in the list, else it'll return “String not found”. If the passed string is present at multiple indices, in that case the function should only return the first index of occurrence.

Considering the above scenario into account, build the logic to print the position of passed string from a given list of strings.

Refer to below instructions and sample input-output for more clarity on the requirement.

Instructions to write main section of the code:

a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence. 


Steps inside main section:

1. Create a list of strings. To create the list,
i. First read the number of elements/strings you want to store in the list.
ii. Read a string and add it to the list. This point repeats for the number of elements/strings to be stored in the list (considered in the first line of input i.e. in point #1.i).

2. Read a string from user which will be searched in the list of strings. Call the function 'searchMyString' and pass the taken input to be searched in the list of strings.

3. Print the output as “Position of the searched string is: ” (excluding quotes, value is the index of first occurence returned by the function).


You can use/refer the below given sample input and output to verify your solution.

Sample Input (below) description:

The first line of input taken in the main section contains an integer value representing the number of elements/strings to be added to the list.

The next lines of inputs are the strings to be added to the list one after another and is repeated for the number of elements/strings given in the first line of input. 
(each line represents one string to be added to the list).

The last line of input is the string which user wants to search in the given list.


Sample Input:

4
Hello Good Morning
abcd123Fghy
India
progoti.c
India


Sample Output:
Position of the searched string is:2
'''

def findString(l, s):
    for i, j in enumerate(l):
        if j == s:
            return i
    return 'String not found'
    

n=int(input())
l=[]
for i in range(n):
    l.append(input())
search=input()

position = findString(l, search)
if type(position) == str:
    print(position)
else:
    print('Position of the searched string is: {}'.format(position))