# wap to read a list form input
# swap the elements in the list of the middle
# Sample case 1
# input [1, 2, 3, 4, 5, 6]
# output [4, 5, 6, 1, 2, 3]

# sample case 2
# input [1, 2, 3, 4, 5]
# output [4, 5, 3, 1, 2]

import math

n = int(input())

l= [] 

for i in range(n):
    l.append(int(input()))

# even number of elements
if n % 2 == 0:
    elements_in_single_half = int(n/2)
    first_half = l[:elements_in_single_half]
    second_half = l[elements_in_single_half:]
    print(second_half+first_half)

# odd number od elements
else:
    middle = int(math.floor(n/2))
    first_half = l[:middle]
    second_half = l[middle+1:]
    print(second_half+[l[middle]]+first_half)