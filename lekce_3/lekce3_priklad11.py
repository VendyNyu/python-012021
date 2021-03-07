#Evidence aut

class Auto:
    def get_info(self):
        if self.vypujcenost:
            print("Můžete si vypůjčit:")
        else:
            print("V současné době není možné si vypůjčit:")
        return f"Auto typu {self.znacka_typvozidla} s registrační značkou {self.registracni_znacka}. Auto má najetých {self.kilometry} kilometrů. "

    def __init__(self, registracni_znacka,znacka_typvozidla, kilometry):
        self.registracni_znacka = registracni_znacka
        self.znacka_typvozidla = znacka_typvozidla
        self.kilometry = kilometry
        self.vypujcenost = True

Auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
Auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

#Test, že to funguje
print(Auto1.get_info())
print(Auto2.get_info())