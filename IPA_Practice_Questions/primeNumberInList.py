import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count

numbers = [2, 3, 5, 7, 10, 13, 15, 17, 20, 23]
print(count_primes(numbers))
