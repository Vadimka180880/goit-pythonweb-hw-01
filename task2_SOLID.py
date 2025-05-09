from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


# Single Responsibility Principle: 
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'


# Interface Segregation Principle:
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# Open-Closed Principle: 
class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logging.info(f"Book '{book.title}' added.")

    def remove_book(self, title: str) -> None:
        book_to_remove = next((book for book in self._books if book.title == title), None)
        if book_to_remove:
            self._books.remove(book_to_remove)
            logging.info(f"Book '{title}' removed.")
        else:
            logging.info(f"Book '{title}' not found.")

    def get_books(self) -> List[Book]:
        return self._books


# Dependency Inversion Principle: 
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            for book in books:
                logging.info(book)
        else:
            logging.info("Library is empty.")


# Usage
if __name__ == "__main__":
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logging.info("Exiting...")
                break
            case _:
                logging.info("Invalid command. Please try again.")
      