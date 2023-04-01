s='Hello'
lst=['Focussed', 'bursts', 'of', 'activity']
print(hasattr(s, '__iter__'))
print(hasattr(s, '__iter__'))
print(hasattr(lst, '__iter__'))
print(hasattr(lst, '__iter__'))
i=iter(s)
j=iter(lst)
print(hasattr(i, '__iter__'))
print(hasattr(i, '__next__'))
print(hasattr(j, '__iter__'))
print(hasattr(j, '__next__'))
