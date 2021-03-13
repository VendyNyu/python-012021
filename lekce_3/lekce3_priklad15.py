#Prodej vstupenek

from datetime import datetime,timedelta

prvni_termin = datetime(2021, 7, 1)
druhy_termin = datetime(2021, 8, 10)
treti_termin = datetime(2021, 8, 11)
ctvrty_termin = datetime(2021, 8, 31)

print("Informace pro uživatele: Datum zadávejte ve formátu den.měsíc.rok, např. 15.7.1995")
uzivatelDatum = input("Zadej datum: ")
uzivatelDatum = datetime.strptime(uzivatelDatum,"%d.%m.%Y")


if prvni_termin <= uzivatelDatum <= druhy_termin:
    uzivatelPocetOsob = int(input("Zadej počet osob: "))
    cenaVstupenky = uzivatelPocetOsob * 250
    print(f"Konečná cena je {cenaVstupenky}.")
elif treti_termin <= uzivatelDatum <= ctvrty_termin:
    uzivatelPocetOsob = int(input("Zadej počet osob: "))
    cenaVstupenky = uzivatelPocetOsob * 180
    print(f"Konečná cena je {cenaVstupenky}.")
else:
    print("Je nám líto. Kino v této době není otevřené.")


