marks = int(input())

if marks >= 80:
    print("{} will grant you a grade A".format(marks))
elif marks >= 60 and marks < 80:
    print("{} will grant you a grade B".format(marks))
elif marks < 60:
    print("{} will grant you a grade C".format(marks))
