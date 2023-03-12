c = { 'CS101' : 'CPP', 'CS102' : 'DS', 'CS201' : 'OOP'}
d = { 'ME126' : 'HPE', 'ME102' : 'TOM', 'ME234' : 'AEM'}

print(c.get('CS102', 'Absent'))
print(c.get('EE102', 'Absent'))
#print(c['EE102'])

c.update(d)
print(c.popitem())
print(c.pop('CS102'))
c.clear()

# nested dict
contacts = {
'Anil': {'DOB' : '17/11/98', 'Favorite' : 'Igloo'},
'Amol': {'DOB' : '14/10/99', 'Favorite' : 'Tundra'},
'Ravi': {'DOB' : '19/11/97', 'Favorite' : 'Artic'}
}

animals={'Tiger':141, 'Lion':152, 'Leopard':110}
birds={'Eagle':38, 'Crow':3, 'Parrot':2}
combined={**animals, **birds}
print(combined)