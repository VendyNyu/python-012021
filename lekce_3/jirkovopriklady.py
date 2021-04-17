# Vrácení auta

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

    def vrat_auto(self, tachometr, dny):
        self.tachometr = self.kilometry + uzivatelKilometry
        self.dny = uzivatelPocetDnu
        if self.dny == 0:
            price = 0
            cenaCelkem = self.dny * price
            self.vypujcenost = True
            return ("Chyba. Zákazník měl auto půjčené 0 dnů!")
        if self.dny < 7:
            price = 400
            cenaCelkem = self.dny * price
            self.vypujcenost = True
            return (f"Stav tachometru po vrácení je {self.tachometr} km. Cena za půjčení je {cenaCelkem} Kč.")
        else:
            price = 300
            cenaCelkem = self.dny * price
            self.vypujcenost = True
            return (f"Stav tachometru po vrácení je {self.tachometr} km. Cena za půjčení je {cenaCelkem} Kč.")

    def __init__(self, registracni_znacka,znacka_typvozidla, kilometry):
        self.registracni_znacka = registracni_znacka
        self.znacka_typvozidla = znacka_typvozidla
        self.kilometry = int(kilometry)
        self.vypujcenost = True



Auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
Auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

print("Informace pro uživatele: Značka auta musí začít velkým písmenem.")

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


uzivatelPocetDnu = int(input("Zadej, jak dlouho měl zákazník auto k dispozici: "))
uzivatelKilometry = int(input("Zadej počet ujetých kilometrů vozidla: "))
if uzivatel == "Peugeot":
    print(Auto1.vrat_auto())
elif uzivatel == "Škoda":
    print(Auto2.vrat_auto())
else:
    print("Chyba. Špatně zadané paramtery.")

"""
#Test, že auto je znovu k dispozici:
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
