'''
Calculate Student Grade

Write a python code as per the below guidelines which will calculate the percenta and grade of a student based on the percentage of marks.
Define a class Student with attributes roll number (roll), student name(name) and a lis which stores the marks scored by the students(marks_list).
Provide following methods to the class:
1. calculate percentage(): This method will calculate the percentage of the student on the basis of the marks obtained by him/her and return the percentage value.
Percentage Calculation:
Percentage Sum of all the marks/Number of subjects
2. find_grade() : This method will find the grade of the student on the basis of the percentage acquired by the student. The method returns the grade of the student.
left
The criteria for grade calculation: 1. If percentage of marks is greater than or
equal to 80, grade is 'A'.
ii. If percentage of marks is greater than or equal to 60 but less than 80, grade is 'B'. iii.percentage of marks is greater than or equal to 40 but less than 60, grade is 'C'. iv. percentage of marks is less than 40, grade is 'F'.
1. Instructions to test your code against your input:
When you want to test your program by providing customized input please follow the below step
Select the check box "Test against custom
input" and input the data as explained in the
text area that is populated after selection of
the check box. a. Provide an integer in the first line of the text area, which represents the numbers of elements to be added in the input list b. Provide the elements one by one in each line after that
c. Click on "Run code" to test your code against your customized input provided as above.
For example1, if you want to give a list of 123
For example1, if you want to give a list of 123 as the student numbet and Rahul as the name and 3 subject marks then then in the text area for customized input, provide the input as follows:

123
Rahul
70
38R8 80
6

Input
80

Note: Third line in the above input represents the number of subjects marks to be entered in the next lines.
Output:

76
B
'''

#!/bin/python3

import math
import os
import random
import re
import sys



#Enter your code here. Read input from STDIN. Print output to STDOUT
class Student:
    def __init__(self, roll, name, marks_list):
        self.roll = roll
        self.name = name
        self.marks_list = marks_list
        
    def calculate_percentage(self):
        percentage = sum(self.marks_list)/len(self.marks_list)
        return int(percentage)
        
    def find_grade(self):
        if self.calculate_percentage() >= 80:
            return 'A'
        elif self.calculate_percentage() >= 60 and self.calculate_percentage() < 80:
            return 'B'
        elif self.calculate_percentage() >= 40 and self.calculate_percentage() < 60:
            return 'C'
        elif self.calculate_percentage() < 40:
            return 'F'
        
        
if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())