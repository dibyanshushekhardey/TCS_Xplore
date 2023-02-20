class Book:
    def __init__(self, id, name, technology):
        self.id=id
        self.name=name
        self.technology=technology

class BookStore:
    def __init__(self, bookDict):
        self.bookdb=bookDict
    
    def serachByTechnology(self, tech):
        abc=[]
        restech=[]
        flag=0
        # traversing the dictionary of object
        for ab in self.bookdb.keys():
            print(self.bookdb[ab].id)
            print(tech)
            print(self.bookdb[ab].technplogy)
            if tech == self.bookdb[ab].technology:
                print(self.bookdb[ab].technology)
                restech.append(self.bookdb[ab]) # adding the object to the list of objects
                flag = 1
        if flag == 0:
            abc.append("NULL")
            abc.append("NULL")
            abc.append("NULL")
            abc.append("NULL")
            restech.append(abc)
        return restech
        
    def compareBooks(self, a,b):
        if a.name == b.name:
            print("Books are same")
        else:
            print("books are not same")


if __name__=='__main__':
    bookdb={}
    bookCount_master=int(input())
    for i in range(bookCount_master):
        id=input()
        name=input()
        technology=input()
        bookObj=Book(id, name, technology)
        bookdb.update({i:bookObj})
    bookStoreObj=BookStore(bookdb)

    technology_searchFor = input()
    restech=bookStoreObj.serachByTechnology(technology_searchFor)
    for k in restech:
        print(k.id)
        print(k.name)
        print(k.technology)
    
    id1 = input()
    name1 = input()
    technology1 = input()
    bookObj1 = Book(id1, name1, technology1)

    id2 = input()
    name2 = input()
    technology2 = input()
    bookObj2 = Book(id2, name2, technology2)

    bookStoreObj.compareBooks(bookObj1, bookObj2)