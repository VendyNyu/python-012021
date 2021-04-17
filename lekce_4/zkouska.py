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
        self.delka = int(delka)
    def get_info(self):
        return super().get_info() + f" Délka filmu je {self.delka} minut."
    def get_celkova_delka(self):
        return self.delka

Film1 = Film("Kamarád taky rád","komedie, romatický",105)
print(Film1.get_info())

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
        super().__init__(nazev, zanr)
        self.pocetEpizod = int(pocetEpizod)
        self.delkaEpizody = int(delkaEpizody)
        self.delka = self.pocetEpizod * self.delkaEpizody
    def get_info(self):
        return super().get_info() + f" Počet epizod seriálu: {self.pocetEpizod} epizod. Epizoda trvá {self.delkaEpizody}"
    def get_celkova_delka(self):
        return self.delka
Serial1 = Serial("Zoufalé manželky","drama, komedie, mysteriózní",108,45)
print(Serial1.get_info())

class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    def pripocti_zhlednuti(self,zhlednutaPolozka):
        self.delka_sledovani += zhlednutaPolozka.delka
        return f"Celkový čas zhlednutí filmů a seriálů je {self.delka_sledovani} minut."

uzivatel1 = Uzivatel("Marek Nový")



















