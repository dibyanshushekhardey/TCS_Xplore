def my_decorator(func):
    def wrapper():
        print('******************')
        func()
        print('~~~~~~~~~~~~~~~~~~~~')
    return wrapper

def display():
    print('I stand decorated')

def show():
    print('Noting great. Me too!')

display=my_decorator(display)
display()
show=my_decorator(show)
show()