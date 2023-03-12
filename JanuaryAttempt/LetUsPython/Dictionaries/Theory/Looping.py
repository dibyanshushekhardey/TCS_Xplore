courses = {'DAA':'CS', 'AOA':'ME', 'SVY':'CE'}

# iertae over key-value pairs
for k, v in courses.items():
    print(k, v)

# ierate over keys
for k in courses.keys():
    print(k)

# ierate ober keys - shorter way
for k in courses:
    print(k)

# iterate over values
for v in courses.values():
    print(v)

# enumerate 
for i, (k, v) in enumerate(courses.items()):
    print(i, k)