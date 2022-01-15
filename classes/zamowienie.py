class Zamowienie:
    _nrzamowienia: int
    _wykonawca: str
    _koszt: float
    _metrymieszkania: int

    def __str__(self):
        return f"Dom nrZamowienia: {self._nrzamowienia}/ Wykonawca: {self._wykonawca}/ Koszt: " \
               f"{self._koszt} Zł/" \
               f" Metry: {self._metrymieszkania}m2 "

    @property
    def nrzamowienia(self) -> int:
        return self._nrzamowienia

    @property
    def wykonawca(self) -> str:
        return self._wykonawca

    @property
    def koszt(self) -> float:
        return self._koszt

    @property
    def metry(self) -> float:
        return self._metrymieszkania

    @nrzamowienia.setter
    def nrzamowienia(self, value):
        self._nrzamowienia = value

    @wykonawca.setter
    def wykonawca(self, value):
        self._wykonawca = value

    @koszt.setter
    def koszt(self, value):
        self._koszt = value

    @metry.setter
    def metry(self, value):
        self._metrymieszkania = value

    def wycena(self, metrydoremontu: float, cenazametr: float) -> float:
        if self._metrymieszkania < metrydoremontu:
            print("bład liczba metrów mieszkania nie moze byc mniejsza niz liczba metrow do remontu")
        else:
            cenaremontu = metrydoremontu*cenazametr
            return round(cenaremontu, 2)
