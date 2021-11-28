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



