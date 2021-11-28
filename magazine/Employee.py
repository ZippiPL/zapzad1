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
