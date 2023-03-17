'''
Write a Python program that is organized as follows:
Packages:
messages.funny
messages.curt
Modules:
modf1.py, modf2.py, modf3.py in package messages.funny
modc1.py, modc2.py, modc3.py in package messages.curt
Functions:
funf1( ) in module modf1
funf2( ) in module modf2
funf3( ) in module modf3
func1( ) in module modc1
func2( ) in module modc2
func3( ) in module modc3
Use all the functions in a program client.py.
Program
Directory structure will be asfollows:
messages
__init__.py
funny
__init__.py
modf1.py
modf2.py
modf3.py
curt
__init__.py
modc1.py
modc2.py
modc3.py
client.py
Of these, messages, funny and curt are directories, rest are files. All
__init__.py files are empty.
'''

import messages.funny.modf1
import messages.funny.modf2
import messages.funny.modf3
import messages.curt.modc1
import messages.curt.modc2
import messages.curt.modc3
messages.funny.modf1.funf1( )
messages.funny.modf2.funf2( )
messages.funny.modf3.funf3( )
messages.curt.modc1.func1( )
messages.curt.modc2.func2( )
messages.curt.modc3.func3( )
