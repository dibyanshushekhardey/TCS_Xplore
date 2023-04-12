class Book:
    def __init__(self, book_id, book_name, author_name):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name


class Library:
    def __init__(self, books_list, address):
        self.books_list = books_list
        self.address = address

    def count_books_by_author(self):
        author_dict = {}
        for book in self.books_list:
            author_name = book.author_name.upper()
            author_dict[author_name] = author_dict.get(author_name, 0) + 1
        return author_dict

def get_books_by_city(city, library_list):
    matching_libraries = []
    for library in library_list:
        if library.address['city'].casefold() == city.casefold():
            matching_libraries.append(library)
    if len(matching_libraries) == 0:
        return None
    books = []
    for library in matching_libraries:
        for book in library.books_list:
            books.append(book)
    sorted_books = sorted(books, key=lambda x: x.book_id, reverse=True)
    return [book.book_name for book in sorted_books]

# main function
if __name__ == '__main__':
    libraries = []
    num_libraries = int(input().strip())

    for i in range(num_libraries):
        books_list = []
        num_books = int(input().strip())
        for j in range(num_books):
            book_id = int(input().strip())
            book_name = input().strip()
            author_name = input().strip()
            books_list.append(Book(book_id, book_name, author_name))
        address = {
            'street': input().strip(),
            'area': input().strip(),
            'city': input().strip(),
            'state': input().strip(),
            'zip': input().strip()
        }
        libraries.append(Library(books_list, address))

    city = input().strip()

    author_dict = libraries[0].count_books_by_author()
    for author, count in author_dict.items():
        print(author, count)

    books_list = get_books_by_city(city, libraries)
    if books_list is None:
        print("No Book Found")
    else:
        print(books_list)