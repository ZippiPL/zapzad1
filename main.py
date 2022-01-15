from classes.zamowienie import Zamowienie
from classes.developer import Developer
# from classes.dom import Dom

developer = Developer("Bartek", "Nowak", 837188912, "Katowice 42-500 graniczna 33")
# dom = Dom(1, "Bedzin czeladzka 1", 5, developer)

zamowieniepierwsza = Zamowienie()
zamowieniepierwsza.nrzamowienia = 1
zamowieniepierwsza.wykonawca = "Firma Drucik"
zamowieniepierwsza._metrymieszkania = 120
zamowieniepierwsza.koszt = zamowieniepierwsza.wycena(20.5, 120.22)

print(zamowieniepierwsza.__str__())
print(developer.__str__())
