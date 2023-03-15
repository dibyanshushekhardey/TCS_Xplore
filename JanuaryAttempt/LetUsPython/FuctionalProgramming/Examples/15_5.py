'''
Following data shows names, ages and marks ofstudents in a class:
Anil, 21, 80
Sohail, 20, 90
Sunil, 20, 91
Shobha, 18, 93
Anil, 19, 85
Write a program to sort this data on multiple keys in the order name,
age and marks.
'''

import operator
lst = [('Anil', 21, 80), ('Sohail', 20, 90), ('Sunil', 20, 91),
('Shobha', 18, 93), ('Anil', 19, 85), ('Shobha', 20, 92)]
print(sorted(lst, key=operator.itemgetter(0, 1, 2)))
print(sorted(lst, key=lambda tpl:(tpl[0],tpl[1], tpl[2])))
