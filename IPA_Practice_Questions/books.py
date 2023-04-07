class Book:
    def __init__(self, bookId, bookName, nameofAuthor):
        self.bookId=bookId
        self.bookName=bookName
        self.nameofAuthor=nameofAuthor

class Library(Book):
    def __init__(self, bookLis, libraryAddress):
        self.bookLis=bookLis
        self.libraryAddress=libraryAddress

    def booksByAuthors(self):
        autDic={}
        autLis=[]
        for obj in self.bookLis:
            autLis.append(obj.nameofAuthor.upper())
        authors=list(set(autLis))
        for aut in authors:
            autDic[aut]=autLis.count(aut)
        return autDic

def findbooktype(city, libObj):
    books=[]
    for obj in libObj:
        for k, v in obj.libraryAddress.items():
            if v == city:
                tempBooks=[]
                for books_obj in obj.bookLis:
                    tempBooks.append(books_obj.bookName)
                tempBooks.reverse()
                books += tempBooks
    return books

libObj=[]
n=int(input())
for _ in range(n):
    bookList=[]
    libraryAddress={}
    for i in range(int(input())):
        bookId=int(input())
        bookName=input()
        nameofAuthor=input()
        bookList.append(bookId, bookName, nameofAuthor)
    libraryAddress['street'] = input()
    libraryAddress['area'] = input()
    libraryAddress['city'] = input()
    libraryAddress['state'] = input()
    libraryAddress['zip'] = input()
    libObj.append(Library(bookList,libraryAddress))

city = input()
for j in range(n):
    obj = libObj[j]
    res = obj.booksByAuthors()
    print(*res.keys(), *res.values())
books = findbooktype(city,libObj)
print(books)

