#https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/slovniky
#Vysvědčení

vysvedceni = {"Český jazyk" : 1, "Matematika" : 1, "Dějepis" : 1}
print(vysvedceni)

#Detektivky
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
#Přidání hodnoty do slovníku:
sales["Noc, která mě zabila"] = 0
print(sales)

#U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100:
sales["Vrah zavolá v deset"] += 100
print(sales)

#Tombola:
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
#Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
uzivatel = int(input("Jaké je tvé číslo lístku? "))

#Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.
if uzivatel in tombola:
    print(f"Gratuluji! Vyhráváš {tombola[uzivatel]} :)")
else:
    print("Bohužel nevyhráváš nic")

#Odeber výhru pro daný lístek ze slovníku, abychom tam evidovali pouze nevydané cen
odebrani = tombola.pop(uzivatel)
print(tombola)

#Paranoidní večírek
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

seznam = input("Zadej své jméno: ")

if seznam in passwords:
    heslo = input("Zadej své heslo: ")
    if heslo in passwords:
        print("Smíš vstoupit.")
    else:
        print("Chybné heslo.")

else:
    print("Bohužel nejsi na seznamu.")
