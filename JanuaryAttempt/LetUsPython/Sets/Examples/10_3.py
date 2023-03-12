'''
Write a program to carry out the following operations on the given set
s = {10, 2, -3, 4, 5, 88}
- number of items in set s
- maximum element in set s
- minimum element in sets
- sum of all elements in sets
- obtain a new sorted set from s, set s remaining unchanged
- report whether 100 is an element of set s
- report whether -3 is an element of set s
'''

s = {10, 2, -3, 4, 5, 88}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
t=sorted(s)
print(t)
print(100 in s)
print(-3 not in s)