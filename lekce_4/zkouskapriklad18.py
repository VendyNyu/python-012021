from datetime import datetime,timedelta

class Kontakt:
   def __init__(self, jmeno, email):
      self.jmeno = jmeno
      self.email = email

class Uchazec(Kontakt):
   def __init__(self, jmeno, email, datum_pohovoru):
      super().__init__(jmeno,email)
      self.datum_pohovoru = datetime.strptime(datum_pohovoru,"%d.%m.%Y")
      self.zapis_z_pohovoru = ""

   def uloz_zapis(self, zapis_z_pohovoru):
      if datetime.now() >= self.datum_pohovoru:
          self.zapis_z_pohovoru = zapis_z_pohovoru
          return "Zápis z pohovoru byl uložen."
      else:
          return "Chyba. Chybí záznam k uložení"



uchazec1 = Uchazec("Jiří Novák", "jirkanovak@gmail.com", "12.3.2021")

print(uchazec1.uloz_zapis("ok"))
