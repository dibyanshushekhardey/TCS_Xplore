'''
Write a recursive function to obtain the running sum of first 25 natural
numbers.
'''

def runningSum(n):
    if n == 0:
        return 0
    else:
        s = n + runningSum(n-1)
        return s
    
max = int(input('Enter the positive largest number for running sum: '))
if max > 0:
    sum = runningSum(max)
    print(f'Running Sum: {sum}')
else:
    print('Entered number is negative')