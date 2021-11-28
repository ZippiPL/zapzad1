class Student:

    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name} z ocenami {self.marks}"

    @property
    def is_passed(self) -> bool:
        return True if self.marks > 50 else False


class Library:
    def __init__(self, city: str, street: str,
                 zip_code: int, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w miescie {self.city} na ulicy " \
               f"{self.street} kod pocztowy {self.zip_code}" \
               f" godziny otwarcia {self.open_hours} " \
               f"numer teleofnu {self.phone} "


class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: str, birth_date: str, city: str,
                 street: str, zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Imie {self.first_name} " \
               f"Nazwisko{self.last_name} " \
               f"Data zatrudnienia {self.hire_date} " \
               f"Data Urodzenia {self.birth_date} " \
               f"Miasto {self.city}" \
               f"Ulica {self.street} " \
               f"Kod pocztowy {self.zip_code}" \
               f" Nr.Telefonu {self.phone}"


class Book:
    def __init__(self, library: Library,
                 publication_date: str, author_surname: str, author_name: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_surname = author_surname
        self.author_name = author_name
        self.number_of_pages = number_of_pages


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


if __name__ == '__main__':
    print("start")
    student_one = Student('Lukasz', 51)
    student_two = Student('Bartek', 49)
    print(student_one.is_passed)
    print(student_two.is_passed)
