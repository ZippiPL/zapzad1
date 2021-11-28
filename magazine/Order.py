import Employee
import Student
import Book


class Order:

    def __init__(self, employee: Employee,
                 student: Student, books: Book, order_date: str):
        self.author_name = None
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Pracownik {self.employee} " \
               f"Student{self.student} " \
               f"Ksiazka {self.books} " \
               f"Data Zamowienia {self.order_date}"


