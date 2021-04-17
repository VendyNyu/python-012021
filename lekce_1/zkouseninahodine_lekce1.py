#1Vysvědčení

vysvedceni = {"Český jazyk": 1, "Matematika": 1, "Dějepis":2}
print(vysvedceni)

#2Detektivky
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

#Přidání do slovníku
sales["Noc, která mě zabila"] = 0

print(sales)

#U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.
sales["Vrah zavolá v deset"] += 100
print(sales)

#Tombola
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

cislolistku = int(input("Zadej číslo svého lístku: "))

if cislolistku in tombola:
    print("JO, vyhráváš")
    tombola.pop(cislolistku)
    print((tombola))

else:
    print("Bohužel nevyhráváš nic.")

#Paranoidní večírek
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

host = input("Zadej své jméno: ")


if host in passwords:
    heslo = str(input("Zadej heslo:"))
    if passwords[host] == heslo:
        print("OK")


else:
    print("Bohužel, nejsi na seznamu.")



