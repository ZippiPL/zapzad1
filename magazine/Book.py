import Library


class Book:
    def __init__(self, library: Library,
                 publication_date: str, author_surname: str, author_name: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_surname = author_surname
        self.author_name = author_name
        self.number_of_pages = number_of_pages
