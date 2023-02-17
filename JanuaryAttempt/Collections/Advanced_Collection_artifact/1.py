# WAP to print sumof input numbers

# traditional approach
numbers = input().split(" ")
nums = []
for i in numbers:
    nums.append(int(i))
numbers = nums.copy()
print(sum(numbers))