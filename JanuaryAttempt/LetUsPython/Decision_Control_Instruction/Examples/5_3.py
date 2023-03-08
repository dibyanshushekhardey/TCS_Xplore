'''
Percentage marks obtained by a student are input through the
keyboard. The student gets a division as per the following rules:
Percentage above or equal to 60 - First division
Percentage between 50 and 59 - Second division
Percentage between 40 and 49 - Third division
Percentage less than 40 - Fail
Write a program to calculate the division obtained by the student.
'''

per=int(input("Enter value of percentage: "))
if per >= 60:
    print("First Division")
elif per >= 50:
    print("Second division")
elif per >= 40:
    print("Third Division")
else:
    print("Fail")