# list comprehension
numbers = input().split(" ")
numbers = [int(i) for i in numbers]
print(sum(numbers))