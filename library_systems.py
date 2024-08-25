# library_system.py

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True  # True means available, False means borrowed

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__availability

    def borrow(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            return True
        return False

    def display_info(self):
        status = "Available" if self.__availability else "Borrowed"
        return (f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, "
                f"Publication Date: {self.__publication_date}, Status: {status}")

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book.get_title())
            return True
        return False

    def return_book(self, book):
        if book.return_book():
            if book.get_title() in self.__borrowed_books:
                self.__borrowed_books.remove(book.get_title())
                return True
        return False

    def display_info(self):
        borrowed = ', '.join(self.__borrowed_books) if self.__borrowed_books else "No borrowed books"
        return (f"Name: {self.__name}, Library ID: {self.__library_id}, "
                f"Borrowed Books: {borrowed}")

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def display_info(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
