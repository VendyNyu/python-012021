#Maturita

vysledky = [
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]


#Spočítání průměru
for prumer in vysledky:
    hodnoty = list(prumer.values())[1:]
    prumer = sum(hodnoty) / 5
    print(prumer)

def ohodnot_studenta(hodnoceni):
    for f in vysledky:
        if prumer <= 1.5 in hodnoceni.values():
            return "vyznamenání"
print(ohodnot_studenta(hodnoceni="Jarka Metelka"))



"""
            def greetUser(name):
                print(f"Ahoj {name}!")

            greetUser("Jirko")
"""










