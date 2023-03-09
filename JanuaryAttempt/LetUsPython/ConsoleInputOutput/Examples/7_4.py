'''
Suppose there are 5 variables in a program—max, min, mean, sd and
var, having some suitable values. Write a program to print these
variables properly aligned using multiple fstrings, but one call to print( ).
'''

minimum, maximum = 25, 75
mean = 35
sd = 0.56
var = 0.9
print(
    f'\n{"Max value: ":<15}{maximum:>10}',
    f'\n{"Min value: ":<15}{minimum:>10}',
    f'\n{"Mean: ":<15}{mean:>10}',
    f'\n{"Std Dev: ":<15}{sd:>10}',
    f'\n{"Variance: ":<15}{var:>10}',
)