d={'Oil':230, 'Clip':150, 'Stud':175, 'Nut':35}
# lambda takes a dictionary item and returns a value
d1=sorted(d.items(), key=lambda kv:kv[1])
print(d1)