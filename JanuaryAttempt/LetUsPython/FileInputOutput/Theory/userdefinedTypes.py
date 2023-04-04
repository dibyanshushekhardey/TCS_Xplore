import json

def encode_complex(x):
    if isinstance(x, complex):
        return (x.real, x.imag)
    else:
        raise TypeError('Complex object is not JSON serializable')

def decode_complex(dct):
    if '__Complex__' in dct:
        return Complex(dct['real'], dct['imag']) 
    return dct

class Complex:
    def __init__(self, r=0, i=0):
        self.real=r
        self.imag=i

    def print_data(self):
        print(self.real, self.imag)

c=Complex(1.0, 2.0)
f=open('data', 'w+')
json.dump(c, f, default=encode_complex)
f.seek(0)
inc=json.load(f, object_hook=decode_complex)
print(inc)