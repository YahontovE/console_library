import json
import os


class Book:
    """Класс содержит метод для преобразования экземпляра книги в словарь и обратно"""

    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Преобразования экземпляра книги в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """Преобразования из словарь в экземпляр книги"""
        return Book(data['id'], data['title'], data['author'], data['year'], data['status'])


class Library:
    """Класс управляет книгами, предоставляет методы для добавления, удаления, поиска, отображения и изменения статуса книг."""

    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Функция на чтение файла с книгами"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]

    def save_books(self):
        """Функция сохранения в файл"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Функция добавления книги в список"""
        book_id = self.generate_id()
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {book_id}.")

    def remove_book(self, book_id):
        """Функция удаления книги по id"""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, search_term):
        """"Функция поиска книиг по критериям """
        results = [book for book in self.books if (search_term.lower() in book.title.lower() or
                                                   search_term.lower() in book.author.lower() or
                                                   search_term == str(book.year))]
        return results

    def display_books(self):
        """Функция выводит все киниг, если они есть"""
        if not self.books:
            print("В библиотеке нет книг.")
            return
        for book in self.books:
            print(f"ID: {book.id}, Название: '{book.title}', Автор: {book.author}, "
                  f"Год: {book.year}, Статус: {book.status}")

    def update_status(self, book_id, new_status):
        """Функция изменения статуса книги"""
        if new_status not in ["в наличии", "выдана"]:
            print("Недопустимый статус. Используйте 'в наличии' или 'выдана'.")
            return
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                print(f"Статус книги с ID {book_id} обновлён на '{new_status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def generate_id(self):
        """Функция генерации id"""
        return max((book.id for book in self.books), default=0) + 1
