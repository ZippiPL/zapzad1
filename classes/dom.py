from developer import Developer


class Dom:
    def __init__(self, nrdomu: int, adres: str, iloscmieszkan: int, wlasciciel: Developer):
        self._nrdomu = nrdomu
        self._adres = adres
        self._iloscmieszkan = iloscmieszkan
        self._wlasciciel = wlasciciel

    def __str__(self):
        return f"Dom: nrDomu {self._nrdomu} Adres {self._adres} iloscMieszkan {self._iloscmieszkan} " \
               f"Wlasciciel {self._wlasciciel} "

    @property
    def nrdomu(self) -> int:
        return self._nrdomu

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def iloscmieszkan(self) -> int:
        return self._iloscmieszkan

    @property
    def wlasciciel(self) -> Developer:
        return self._wlasciciel
