'''
From a dictionary with string keys create a new dictionary with the
vowels removed from the keys.
'''

words = {'Tub':1, 'Toothbrush':2, 'Towel':3, 'Nailcutter':4}
d={''.join(alpha for alpha in k if alpha not in 'aeiou'):v for (k, v) in words.items()}
print(d)