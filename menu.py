# menu.py

import re
from library_system import Book, User, Author

# In-memory storage
books = {}
users = {}
authors = {}

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    book = Book(title, author, genre, publication_date)
    books[title] = book
    print("Book added successfully!")

def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    user_id = input("Enter your library ID: ")
    user = users.get(user_id)
    book = books.get(title)
    if user and book:
        if user.borrow_book(book):
            print("Book borrowed successfully!")
        else:
            print("Book could not be borrowed. It may be unavailable.")
    else:
        print("Invalid book title or user ID.")

def return_book():
    title = input("Enter the title of the book to return: ")
    user_id = input("Enter your library ID: ")
    user = users.get(user_id)
    book = books.get(title)
    if user and book:
        if user.return_book(book):
            print("Book returned successfully!")
        else:
            print("Book could not be returned. It may not be borrowed by you.")
    else:
        print("Invalid book title or user ID.")

def search_book():
    title = input("Enter the title of the book to search: ")
    book = books.get(title)
    if book:
        print(book.display_info())
    else:
        print("Book not found.")

def display_all_books():
    if books:
        for book in books.values():
            print(book.display_info())
    else:
        print("No books available.")

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    user = User(name, library_id)
    users[library_id] = user
    print("User added successfully!")

def view_user_details():
    library_id = input("Enter library ID to view details: ")
    user = users.get(library_id)
    if user:
        print(user.display_info())
    else:
        print("User not found.")

def display_all_users():
    if users:
        for user in users.values():
            print(user.display_info())
    else:
        print("No users available.")

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    author = Author(name, biography)
    authors[name] = author
    print("Author added successfully!")

def view_author_details():
    name = input("Enter author name to view details: ")
    author = authors.get(name)
    if author:
        print(author.display_info())
    else:
        print("Author not found.")

def display_all_authors():
    if authors:
        for author in authors.values():
            print(author.display_info())
    else:
        print("No authors available.")

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Select an option (1-4): ")
        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Return to Main Menu")

        choice = input("Select an option (1-6): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Return to Main Menu")

        choice = input("Select an option (1-4): ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Return to Main Menu")

        choice = input("Select an option (1-4): ")
        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
