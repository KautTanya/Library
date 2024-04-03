"""Library"""
import re


class User:
    """User"""
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


class Book:
    """Book"""
    total_copies = 0

    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        Book.total_copies += copies

    def check_availability(self):
        """Перевіряємо чи є книга у бібліотеці"""
        return self.copies > 0

    @classmethod
    def update_total_copies(cls, book):
        """Оновлюємо загальну кількість копій книжок коли вони будуть змінюватись"""
        cls.total_copies += book

    def update_copies(self, new_count_book):
        """Оновлюємо кількість книжок у конкретній бібліотеці"""
        Book.total_copies += new_count_book - self.copies
        self.copies = new_count_book

    def validate_isbn(self):
        """Валідуємо правильність isbn коду(ISBN 0-061-96436-0)"""
        pattern = re.match(r"^ISBN\s\d-\d{3}-\d{5}-\d$", self.isbn)
        if pattern:
            return "True"
        else:
            return "ISBN is not validate"


class Library:
    """Library"""
    def __init__(self):
        self.books = []
        self.users = []

    def add_user(self, user):
        """Реєструємо користувача у бібліотеці"""
        self.users.append(user)
        return f"{user.name} registered in the library"

    def find_book(self, isbn):
        """Знаходимо книжку за isbn"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return "This book is not in library"

    def show_all_books(self):
        """Показуємо всі доступні книжки у бібліотеці"""
        all_books = [book for book in self.books]
        return all_books


class Customer(User):
    """Customer"""
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        """borrow book"""
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_copies(book.copies - 1)
            return f"{self.name} borrowed {book.title}"
        else:
            return f"This {book.title} is not in library"

    def return_book(self, book):
        """return book"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_copies(book.copies + 1)
            return f"{self.name} returned {book.title}"
        else:
            return f"You did not borrow this {book.title}"


class Employee(User):
    """Employee"""

    def __init__(self, name, user_id, salary):
        super().__init__(name, user_id)
        self.__salary = salary

    @staticmethod
    def add_book(lib, book):
        """Add book"""
        lib.books.append(book)
        return f"{book.title} added to the library"

    @staticmethod
    def remove_book(lib, book):
        """Remove book"""
        if book in lib.books:
            lib.books.remove(book)
            Book.update_total_copies(-book.copies)
            return f"{book.title} removed from the library"
        else:
            return f"{book.title} is not in the library"


library = Library()
user1 = Customer("John Doe", 1001)
user2 = Customer("Alice Smith", 1002)

print(library.add_user(user1))
print(library.add_user(user2))

book1 = Book("Python Programming", "Guido van Rossum", "ISBN 978-1-118-92278-4", 5)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN 978-0-7432-7356-5", 3)

print(Employee.add_book(library, book1))
print(Employee.add_book(library, book2))

print(Employee.remove_book(library, book2))

print(user1.borrow_book(book1))
print(user2.borrow_book(book1))

print(user1.return_book(book1))

library.books = [book1, book2]

print(library.find_book("ISBN 978-1-118-92278-4"))
print(library.find_book("ISBN 978-0-7432-7356-5"))

library.books = [book1, book2]
print(library.show_all_books())
