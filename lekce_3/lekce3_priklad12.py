#Půjčení auta

class Auto:
    def pujc_auto(self):
        if self.vypujcenost:
            print("Potvrzuji zapůjčení vozidla.")
            self.vypujcenost = False
        else:
            print("Vozidlo není k dispozici.")

    def get_info(self):
        return f"Informace k autu: Značka a typ vozidla - {self.znacka_typvozidla}, registrační značka -  {self.registracni_znacka}."

    def __init__(self, registracni_znacka,znacka_typvozidla, kilometry):
        self.registracni_znacka = registracni_znacka
        self.znacka_typvozidla = znacka_typvozidla
        self.kilometry = kilometry
        self.vypujcenost = True


Auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
Auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

uzivatel = input("Zadejte značku auta, kterou si chcete půjčit: ")
if uzivatel == "Peugeot":
    print(Auto1.get_info())
    Auto1.pujc_auto()
elif uzivatel == "Škoda":
    print(Auto2.get_info())
    Auto2.pujc_auto()
else:
    print("Auto není v naší půjčovně k dispozici.")

"""
#Test, že funkce pujc_auto nedovolí půjčit stejné auto dvakrát:

uzivatel = input("Zadejte značku auta, kterou si chcete půjčit: ")
if uzivatel == "Peugeot":
    print(Auto1.get_info())
    Auto1.pujc_auto()
elif uzivatel == "Škoda":
    print(Auto2.get_info())
    Auto2.pujc_auto()
else:
    print("Auto není v naší půjčovně k dispozici.")
"""
