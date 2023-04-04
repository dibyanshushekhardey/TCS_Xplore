'''
Write a program to read the contents of file 'messages' one character at
a time. Print each character that is read.
'''

f=open('messages', 'r')
while True:
    data=f.read(1)
    if data=='':
        break
    print(data, end='')

f.close()
