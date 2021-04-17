class Employee:
    # fce na dovolenou - třeba vybrání dovolené
    def take_holiday(self, days):
        if self.holidays >= days:
          self.holidays = self.holidays - days
          return "Dovolená schválená"
        else:
            return f"Můžeš si vzít pouze {self.holidays} dnů"


    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}"
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.holidays = 25
#fce init ve chvíli, kdy vytvářím objekt, tak s nimi začně pracovat
#name je parametr fce init, Tak to můžu měnit v té fci init něco jako řádek 12 a 24. Jak jsme tam psali dvakrát. Je to univerzání fce a můžu, tak vyplňovat to v té fci.
# self. holidays = 25 - firma má prostě 25 dnů je to tam natvrdo, nebudu to měnit
#atribut poznáš, že to začíná self.
#fce --str
"""
#Tvoření zaměstnance:
frantisek = Employee()
frantisek.name = "František Novák"
frantisek.position = "kontruktér"
frantisek.get_info()
print(frantisek.get_info())

#Fce nám vyhodí řetězec
#Máme jednu třídu z té může být více objektů

klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstruktérka"
print(klara.get_info())

#Nyní jsou tu dva objekty, které jsou na sobě nezávislé
"""
#Zkrácený zápis lepší pro programátory
frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "konstruktérka")
print(frantisek)
print(frantisek.get_info())
print(frantisek.take_holiday(80))
print(frantisek.take_holiday(10))

#speciální fce __str__ hledá ve chvíli, kdy převádím objekt či třídu. Třídu to, ale musím naučit
"""
def__str__(self):
  return.self.name 
  - vypíše to František Novák
  Použiji str, když chci, aby se mi objekt reálně vypsal
  
def __str__(self):
   return self.name + "," + self.position + "," + str(self.holidays)
   - to by mi napsalo všechny informace, které potřebuji 
   teoreticky by to šlo i cyklem 
   
kdybych chtěla vytvořit slovník 
print(frantisek.__dict__) přišla bych ale o fce, ale zobrazí mi to atributy
"""

