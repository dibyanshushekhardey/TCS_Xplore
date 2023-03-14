'''
Write a program that defines a function called frequency( ) which
computes the frequency of words present in a string passed to it. The
frequencies should be returned in sorted order by words in the string.
'''

def frequency(s):
    freq={}
    for word in s.split():
        freq[word]=freq.get(word, 0)+1
    return freq

sentence='It is true for all that that that that\
that that that refers to is not the same that\
that that that refers to'
d=frequency(sentence)
words=sorted(d)

for w in words:
    print('%s:%d'%(w, d[w]))