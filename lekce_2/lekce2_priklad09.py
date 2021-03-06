#Maturita

vysledky = [
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

#Spočítat průměr jednotlivých žáků


def ohodnot_studenta(vysledky):
        hodnoty = list(vysledky.values())[1:]
        prumer = sum(hodnoty) / 5
        #print(prumer)

        if prumer <= 1.5 and 3 not in vysledky.values():
            return "Prospěl s vyznamenáním"
        elif 5 in vysledky.values():
            return "Neprospěl"
        else:
            return "Prospěl"


for student in vysledky:
    prospech = ohodnot_studenta(student)
    print(f"{student['Jméno']} : {prospech}")








"""
část fungujícího kodu 
def ohodnot_studenta(vysledky):
    for prospech in vysledky:
        hodnoty = list(prospech.values())[1:]
        prumer = sum(hodnoty) / 5
        #print(list(prospech.values())[1:])
        #print(prospech["Jméno"])
        print(prumer)

print(ohodnot_studenta(vysledky))
"""











