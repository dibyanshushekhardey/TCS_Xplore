f=open('numbertxt', 'w+')
f.write(str(233)+'\n')
f.write(str(13.45))
f.seek(0)
a=int(f.readline())
b=float(f.readline())
print(a+a)
print(b+b)
