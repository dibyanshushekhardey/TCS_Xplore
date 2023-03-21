# outer function
def display():
    a=500
    print('Saving is the best thing')

    # inner functions
    def show():
        print('Especially when your parents have done it for you!')
        print(a)

    show()
display()