'''
Write a program to implement a Queue data structure. Queue is a First
In First Out (FIFO) list, in which addition takes place at the rear end of
the queue and deletion takes place at the front end of the queue.
'''

import collections
q = collections.deque()

q.append('Suhana')
q.append('Shabana')
q.append('Shakila')
q.append('Shakira')
q.append('Sameera')
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)