'''
umbers in the range 15 to 45. Count how many of these numbers are
lessthan 30. Delete all numbers which are less than 30.
'''

import random
r={int(15+30 * random.random()) for num in range(10)}
print(r)

count=len({num for num in r if num < 30})
print(count)

s = {num for num in r if num < 30}
r = r - s
print(r)

