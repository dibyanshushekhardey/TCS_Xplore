# demonstrate how to create simple and multi-line strings and whether a string can change after creation.
# also show the usage of built-in functions len(), min() and max() on a string

# simple strings
msg1='Hoopla'
print(msg1)

#strings with special characters
msg2='He said, \'Let us Python\'.'
file1='C:\\DSD\\newfile'
file2=r'C:\DSD\newfile'
print(msg2)
print(file1)
print(file2)

# multiline strings
# whilespace at beginning of second line becomes part of string
msg3='What is this life of full of care...\
    We have no time to stand and stare'
# enter at the end of first line becomes part od string
msg4="""What is this life if full of care...
We have no time to stand and stare"""

# strings are concatenated properly. () necessary
msg5=('What is thos life if full of care...'
      'We have no time to stand and stare')
print(msg3)
print(msg4)
print(msg5)

# string replication during printing
msg6='MacLearn!!'
print(msg1*3)

#immutability of strings
# utopia cannot change, msg7 can
msg7='Utopia'
msg8='Today!!!'
msg7 = msg7+msg8
print(msg7)

# use of built in functions on strings
print(len('Hoopia'))
print(min('Hoopla'))
print(max('Hoopla'))