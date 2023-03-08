'''
While purchasing certain items, a discount of 10% is offered if the
quantity purchased is more than 1000. If quantity and price per item are
input through the keyboard, write a program to calculate the total
expenses.
'''

qty=int(input("Enter value of quantity: "))
price=float(input("Enter value of price: "))
if qty > 1000:
    dis = 10
else:
    dis = 0
totexp=qty * price - qty * price * dis / 100
print("Total expenses=Rs. "+str(totexp))
