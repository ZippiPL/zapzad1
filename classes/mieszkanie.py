from dom import Dom
from developer import Developer


class Mieszkanie (Dom):

    def __init__(self, nrmieszkania: int, imieinazwisko: str, iloscpokoi: int, wlasciciel: Developer,
                 adres: str, iloscmieszkan, nrdomu: int):
        self._nrmieszkania = nrmieszkania
        self._imieinazwisko = imieinazwisko
        self._wlasciciel = wlasciciel
        self._iloscpokoi = iloscpokoi
        super().__init__(nrdomu, adres, iloscmieszkan, wlasciciel)

    def __str__(self):
        return f"Mieszkanie: ImieWlasciciela {self._imieinazwisko} NazwiskoWlasciciela" \
               f" {self._wlasciciel} nrMieszkania " \
               f"{self._nrmieszkania} " \
               f"ilosc pokoi {self._iloscpokoi}"

    @property
    def nrmieszkania(self) -> int:
        return self._nrmieszkania

    @property
    def imieinazwisko(self) -> str:
        return self._imieinazwisko

    @property
    def wlasciciel(self) -> Developer:
        return self._wlasciciel

    @property
    def iloscpokoi(self) -> int:
        return self._iloscpokoi
