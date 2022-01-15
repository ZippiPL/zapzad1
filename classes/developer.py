class Developer:

    def __init__(self, imie: str, nazwisko: str, pesel: int, adres: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._pesel = pesel
        self._adres = adres

    def __str__(self):
        return f"Developer: Imie {self._imie} Nazwisko {self._imie} Pesel {self._pesel} Adres {self._adres} "

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def pesel(self) -> int:
        return self._pesel

    @property
    def adres(self) -> str:
        return self._adres
