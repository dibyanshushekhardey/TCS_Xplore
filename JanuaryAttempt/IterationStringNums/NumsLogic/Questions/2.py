#WAP to find if the input is prime or not
n = int(input())
if n > 1:
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")