# base class
class Index:
    def __init__(self):
        self._count=0
    def display(self):
        print('count='+str(self._count))
    def incr(self):
        self._count += 1

# derived class
class newIndex(Index):
    def __init__(self):
        super().__init__()

    def decr(self):
        self._count -= 1

i=newIndex()
i.incr()
i.incr()
i.incr()
i.display()
i.decr()
i.display()
i.decr()
i.display()


