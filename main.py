import time

from utils import Library


def main():
    """Функция основной программы взаимодействия с пользователем"""
    library = Library()

    while True:
        print("\n==== Управление библиотекой ====")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)
        elif choice == '3':
            search_term = input("Введите название, автора или год для поиска: ")
            results = library.search_books(search_term)
            if results:
                print("Результаты поиска:")
                for book in results:
                    print(f"ID: {book.id}, Название: '{book.title}', Автор: {book.author}, "
                          f"Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.update_status(book_id, new_status)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")
        time.sleep(2)


if __name__ == "__main__":
    main()
