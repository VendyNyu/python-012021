class Polozka:
    def get_info(self):
        return f"{self.nazev} je žánr - {self.zanr}."

    def __init__(self,nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

polozka1 = Polozka("Harry Potter", "fantasy")

print(polozka1.get_info())

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def get_info(self):
        return super().get_info() + f" Délka filmu je {self.delka} minut."

Film1 = Film("Kamarád taky rád","komedie, romatický","105")
print(Film1.get_info())

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
        super().__init__(nazev, zanr)
        self.pocetEpizod = pocetEpizod
        self.delkaEpizody = delkaEpizody
    def get_info(self):
        return super().get_info() + f" Počet epizod seriálu: {self.pocetEpizod} epizod. Epizoda trvá {self.delkaEpizody}"
Serial1 = Serial("Zoufalé manželky","drama, komedie, mysteriózní","108","41-45 minut")
print(Serial1.get_info())



