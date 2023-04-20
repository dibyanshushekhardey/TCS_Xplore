'''
Create a class pan .
Make attributes id , string
material , string
brand , string
price , int
capacity , int

Write constructor having argument in 
same order as above . 

Write the solution class
 and write main method
implement two static functions 
namely (costliest pan) and 
(discounted price) in it. 

Costliest pan function : 
It accepts 2 arguments , 
namely the array of pan class 
objects and material of a pan . 
It return the costliest pan 
of the given material.

Discounted price : 
It accepts 2 arguments , 
namely , array of pan objects and brand of pan . 
If capacity of given brand > 500 ml , 
update price to 20% discount . 
If capacity > 1000 ml , 
then update price to 26% discount . 


In the main function , 
take input of variable for 7 class objects . 
Take material as input , 
then take brand as input 
for passing to different functions. 
Call the costliest pan 
function , print the id of the 
object returned. 
Call the discounted price function , 
print the new value after updating . 



Input:

7
id23
brass
a
200
120
id24
cupper
b
300
1130
id25
chromium
c
400
640
id26
steel
d
500
950
id27
steel
e
800
950
id28
iron
f
500
950
id29
aluminum
g
500
950
steel
d


output:

id27
400


'''

class Pan:
    def __init__(self, id1, material, brand, price, capacity):
        self.id1=id1
        self.material=material
        self.brand=brand
        self.price=price
        self.capacity=capacity

class Solution:
    @staticmethod
    def costliestPan(lst_pan, inpt_material):
        cost=[]
        for i in lst_pan:
            if i.material.lower()==inpt_material:
                cost.append(i.price)
        if cost==[]:
            print('No pan with the given material')
        else:
            for j in lst_pan:
                if j.price == max(cost):
                    print(j.id1)
    
    @staticmethod
    def discountedPrice(lst_pan, inpt_brand):
        for i in lst_pan:
            if i.brand.lower() == inpt_brand.lower():
                if 1000 > i.capacity > 500:
                    i.price -= i.price*0.2
                    print(int(i.price))
                if i.capacity > 1000:
                    i.price -= i.price * 0.26
                    print(int(i.price))

n=int(input())
lst_pan = []
for i in range(n):
    id1=input()
    material=input()
    brand=input()
    price=int(input())
    capacity=int(input())
    lst_pan.append(Pan(id1, material, brand, price, capacity))
inpt_material=input()
inpt_brand=input()
Solution.costliestPan(lst_pan, inpt_material)
Solution.discountedPrice(lst_pan, inpt_brand)