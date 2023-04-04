import json
lofl=[10, [20, 30, 40], [50, 60, 70], 80, 90]
f=open('data', 'w+')
json.dump(lofl, f)
f.seek(0)
inlofl=json.load(f)
print(inlofl)
f.close()

# serialise deserialise a dictionary
import json
contacts={
    'Anil': { 'DOB' : '17/11/98', 'Favorite' : 'Igloo' },
'Amol': { 'DOB' : '14/10/99', 'Favorite' : 'Tundra' },
'Ravi': { 'DOB' : '19/11/97', 'Favorite' : 'Artic' } 
}
f=open('data', 'w+')
json.dump(contacts, f)
f.seek(0)
incontacts=json.load(f)
print(incontacts)
f.close()