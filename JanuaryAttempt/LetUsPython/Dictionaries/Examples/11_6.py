'''
Suppose there are two dictionaries called boys and girls containing
names as keys and ages as values. Write a program to merge the two
dictionaries into a third dictionary
'''

boys = {'Nilesh':41, 'Soumitra':42, 'Nadeem':47}
girls={'Rasika':38, 'Rajashree':43, 'Rasika':45}
combined={**boys, **girls}
print(combined)
combined={**girls, **boys}
print(combined)
