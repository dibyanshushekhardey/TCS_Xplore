'''
Write a Python program that reports the time of creation, time of last
access and time of last modification for a given file.
'''

import os, time

file='sampledata'
print(file)

created=os.path.getctime(file)
modified=os.path.getmtime(file)
accessed=os.path.getatime(file)

print('Data created:'+time.ctime(created))
print('Data modified:'+time.ctime(modified))
print('Data accessed:'+time.ctime(accessed))
