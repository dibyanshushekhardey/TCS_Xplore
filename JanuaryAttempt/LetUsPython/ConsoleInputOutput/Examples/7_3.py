'''
Write a program to maintain names and cell numbers of 4 persons and
then print them systematically in a tabular form.
'''

contacts = {
    'Dilip':2223334444, 'Shekhar': 4445556666,
    'Vivek': 6667778888, 'Riddhi':8889990000
}

for name, cellno in contacts.items():
    print(f'{name:15}:{cellno:10d}')