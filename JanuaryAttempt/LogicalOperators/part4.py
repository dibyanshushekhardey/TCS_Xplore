# check the marks year and age of a student

marks = int(input())
year = int(input())
age = int(input())

if marks > 80 and year < 2020 and age > 18:
    print("{}:true".format(age))
else:
    print("{}:false".format(age))