eng = 'A B C D'
dev='अ आ इ ई'
print(type(eng))
print(type(dev))
print(eng)
print(dev)
print (eng.encode('utf-8') )
print (eng.encode('utf-16') )
print (dev.encode('utf-8') )
print (dev.encode('utf-16') )
print(b'A B C D'.decode('utf-8'))
print(b'\xff\xfeA\x00 \x00B\x00 \x00C\x00 \x00D\x00'
.decode('utf-16'))
print(b'\xe0\xa4\x85 \xe0\xa4\x86 \xe0\xa4\x87\xe0\xa4\x88'
.decode('utf-8'))
print(b'\xff\xfe\x05\t \x00\x06\t \x00\x07\t \x00\x08\t'
.decode('utf-16'))