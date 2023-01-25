a = int(input())
b = int(input())

choice = int(input())

if choice == 1:
    print("{} + {} = {}".format(a, b, a+b))
elif choice == 2:
    print("{} - {} = {}".format(a, b, a-b))
elif choice == 1:
    print("{} ^ {} = {}".format(a, b, a**b))
elif choice == 1:
    print("{} * {} = {}".format(a, b, a*b))
else:
    print("Invalid choice! Exiting Application!")