'''
Create a class Weather that has a list containing weather parameters.
Define an overloaded in operator that checks whether an item is present
in the list.
'''

class Weather:
    def __init__(self):
        self.__params=['Temp', 'Rel Hum', 'Cloud Cover', 'Wind Vel']
    def __contains__(self, p):
        return True if p in self.__params else False

w=Weather()
if 'Rel Hum' in w:
    print('Valid weather parameter')
else:
    print('Invalid weather parameter')