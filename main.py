class Produkt:


    def __init__(self, id: int, product_name: str, quantity: int, value: float, made_by: str,):
        self._id = id
        self._product_name = product_name
        self._quantity = quantity
        self._value = value
        self._made_by = made_by

    def __str__(self):
        return f"Id Produktu - {self._id}/ Produkt - {self._product_name}  Ilosc Produktu - {self._quantity}  Cena - {self._value} Firma Wykonwacza - {self._made_by} "

    @property
    def id(self):
        return self._id

    @property
    def product_name(self):
        return self._product_name

    @property
    def value(self):
        return self._value

    @property
    def made_by(self):
        return self._made_by

    @property
    def quantity(self):
        return self._quantity

    @id.setter
    def id(self, value):
        self._id = value

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @value.setter
    def value(self, value):
        self._value = value

    @made_by.setter
    def made_by(self, value):
        self._made_by = value


class Magazyn:

    def __init__(self, id : id, adress: str, list_of_products: list, contact_number: int,):
        self._id = id
        self._adress = adress
        self._list_of_products = list_of_products
        self._contact_number = contact_number

    def __str__(self):
        return f"ID magazynu - {self.id}/ Adress - {self.adress}  Lista Produktow - {self.list_of_products}  Numer Kontaktowy- {self.contact_number} "

    @property
    def id(self):
        return self._id

    @property
    def adress(self):
        return self._adress

    @property
    def list_of_products(self):
        return self._list_of_products

    @property
    def contact_number(self):
        return self._contact_number

    @id.setter
    def id(self, value):
        self._id = value

    @adress.setter
    def adress(self, value):
        self._adress = value

    @list_of_products.setter
    def list_of_products(self, value):
        self._list_of_products = value

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value


class Zamowienie:

    def __init__(self, order_number: int, client_type: int, list_of_products, contact_number:int, delivery_adress: str):
        self._order_number = order_number
        self._client_type = client_type
        self._list_of_products = list_of_products
        self._contact_number = contact_number
        self._delivery_adress = delivery_adress

    def __str__(self):
        return f" Numer Zamowienia- {self._order_number}/ Typ Klienta - {self._client_type}  Lista Produktow - {self._list_of_products}  Numer Kontaktowy- {self._contact_number} "

    def count_price(self,price_product:float,quantity:int) -> float:
        return price_product*quantity



    @property
    def order_number(self):
        return self._order_number

    @property
    def delivery_adress(self):
        return self._delivery_adress

    @property
    def client_type(self):
        return self._client_type

    @property
    def list_of_products(self):
        return self._list_of_products

    @property
    def contact_number(self):
        return self._contact_number

    @order_number.setter
    def order_number(self,order_number: int):
        self._order_number = order_number
        print(" Zmieniono numer zamowienia")

    @client_type.setter
    def client_type(self, client_type: int):
        self._client_type = client_type
        print(" Zmieniono typ clienta")

    @list_of_products.setter
    def list_of_products(self, product_list: list):
        self._list_of_products = product_list
        print(" Zmieniono wartość w liscie produktów")

    @contact_number.setter
    def contact_number(self, contact_number: int):
        self._contact_number = contact_number
        print(" Zmieniono wartość Numer Kontaktowy")




class Klient:

    def __init__(self, imie : str, nazwisko : str , phone_number: int, delivery_adress: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._phone_number = phone_number
        self._delivery_adress = delivery_adress

    def __str__(self):
        return f" Imie- {self.imie}/ Nazwisko - {self.nazwisko}  Numer Telefonu - {self.phone_number}  Adres do dostarczenia - {self.delivery_adress} "


    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def delivery_adress(self):
        return self._delivery_adress


    @delivery_adress.setter
    def delivery_adress(self, delivery_adress: str):
        self._delivery_adress = delivery_adress
        print(" Zmieniono Adres dostawy")

    @phone_number.setter
    def phone_number(self, phone_number: int):
        self._phone_number = phone_number
        print(" Zmieniono Number Telefonu")

    @imie.setter
    def imie(self, imie: str):
        self._imie = imie
        print(" Zmieniono Imie")

    @nazwisko.setter
    def nazwisko(self, nazwisko: str):
        self._nazwisko = nazwisko
        print(" Zmieniono Nazwisko")


class KlientBiznesowy(Klient):

    def __str__(self):

        print("Jestem klientem biznesowym")

class KlientDetaliczny(Klient):

    def __str__(self):

        print("Jestem klientem Detalicznym")


produkt_pierwszy = Produkt(1,"Plyta msi",5, 500.0, "MSI")
produkt_drugi = Produkt(2,"Plyta amd",15, 300.0, "AMD")
produkt_trzeci = Produkt(3,"Plyta intel",20, 2500.0, "INTEL")

print(f"{produkt_pierwszy.__str__()}")
print(f"{produkt_drugi.__str__()}")
print(f"{produkt_trzeci.__str__()}")

klient_pierwszy_detaliczny = KlientDetaliczny("Lukasz","Nielaba",333333333,"Gliwice 42-512 Piastow 1")
klient_drugi_biznesowy = KlientBiznesowy("Denis","Duda",555555555,"Psary 42-512 Graniczna 1")


klient_pierwszy_detaliczny.__str__()
klient_drugi_biznesowy.__str__()


