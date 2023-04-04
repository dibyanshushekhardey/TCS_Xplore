# serialise/deserialise a list
import json
f=open('sampledata', 'w+')
lst=[10, 20, 30, 40, 50, 60, 70, 80, 90]
json.dump(lst, f)
f.seek(0)
inlst=json.load(f)
print(inlst)
f.close()

# serialise/deserialise a tuple
import json
f = open('sampledata', 'w+')
tpl = ('Ajay', 23, 2455.55)
json.dump(tpl, f)
f.seek(0)
intpl = json.load(f)
print(tuple(intpl))
f.close()

# serialize/deserialize a dictionary
import json
f = open('sampledata', 'w+')
dct = { 'Anil' : 24, 'Ajay' : 23, 'Nisha' : 22}
json.dump(dct, f)
f.seek(0)
indct = json.load(f)
print(indct)
f.close()