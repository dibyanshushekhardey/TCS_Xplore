'''
Create a class Laptop with the below attributes:

laptopId - int
brand - String
osType - String
price - double
rating - int

The above attributes should be private, write getters, setters and parameterized constructor as required.

Create class Solution with main method.

Implement two static methods - countOfLaptopsByBrand and searchLaptopByOsType in Solution class.

countOfLaptopsByBrand method:
This method will take two input parameters - array of Laptop objects and a String parameter.
The method will return the count of laptops from array of Laptop object for the given brand(String parameter passed) whose rating is more than 3.
If no Laptop with the above condition is present in the array of Laptop objects, then the method should return 0.

searchLaptopByOsType method:
This method will take two input parameters - array of Laptop objects and a String parameter.
The method will return Laptop object array in an descending order of their laptopId, from the array of Laptop objects whose os attribute matches with the given OS(String parameter passed).
If no Laptop with the given OS is present in the array of Laptop objects, then the method should return null.

Note : No two Laptop object would have the same laptopId.
All the searches should be case insensitive.

The above mentioned static methods should be called from the main method.

For countOfLaptopsByBrand method - The main method should print the count of laptops as it is, if the returned value is greater than 0, or it
should print "The given brand is not available".

For searchLaptopByOsType method - The main method should print the laptopId and rating from the returned Laptop object array if the returned value is not null.
If the returned value is null then it should print "The given os is not available".

Before calling these static methods in main, use Scanner object to read the values of Four Laptop objects referring attributes in the above mentioned attribute sequence. 
Next, read two String values for capturing brand and os.


Consider below sample input and output:
TestCase1:
Input:
123
HP
Windows
35000
5
124
Apple
Mac OS
70000
5
125
Dell
Ubuntu
30000
4
126
HP
windows
40000
4
HP
windows

Output:
2
126
4
123
5


TestCase2:
Input:
123
HP
Windows
35000
5
124
Apple
Mac OS
70000
5
125
Dell
Ubuntu
30000
4
126
Asus
windows
40000
3
HP1
Ubuntu1

Output:
The given brand is not available
The given os is not available

'''

class Laptop:
    def __init__(self, laptopId, brand, osType, price, rating):
        self.laptopId=laptopId
        self.brand=brand
        self.osType=osType
        self.price=price
        self.rating=rating
    
class Solution:
    @staticmethod
    def countOfLaptopByBrand(lst_laptop, inpt_brand):
        count = 0
        for i in lst_laptop:
            if i.brand.lower()==inpt_brand.lower() and i.rating > 3:
                count += 1
        if count == 0:
            print('The given brand is not avilable')
        else:
            print(count)

    @staticmethod
    def searchLaptopByOsType(lst_laptop, inpt_os):
        lst_laptop=sorted(lst_laptop, key=lambda x:x.laptopId, reverse=True)
        lap=[]
        for i in lst_laptop:
            if i.osType.lower() == inpt_os.lower():
                lap.append(i)
        if lap == []:
            print('The given os is not available')
        else:
            for j in lap:
                print(j.laptopId)
                print(j.rating)

n = int(input())
lst_laptop=[]
for i in range(n):
    laptopId=int(input())
    brand=input()
    osType=input()
    price=float(input())
    rating=int(input())
    lst_laptop.append(Laptop(laptopId, brand, osType, price, rating))

inpt_brand=input()
inpt_os=input()

Solution.countOfLaptopByBrand(lst_laptop, inpt_brand)
Solution.searchLaptopByOsType(lst_laptop, inpt_os)

