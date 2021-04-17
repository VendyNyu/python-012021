"""
#Čtenářský deník
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
#Celkový počet stran, které gustav přečetl
read = 0

for item in books:
    read += item["pages"]

print(f"Celkem přečetl {read} stran.")

#Počet knih, kterým dal Gustav hodnocení alespoň 8

for item in books:
    if item["rating"] >= 8:
        print(item)

print(f"Dobré hodnocení mají {celkem} knihy")

#Vysvědčení
schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}
#Napiš program, který spočte průměrnou známku ze všech předmětů.
secteneznamky = 0
for key, value in schoolReport.items():
    secteneznamky += value
    ok = len(key)

#Zeptat se učitele vychází mi len 6

print(secteneznamky)
print(ok)

#Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
for key, value in schoolReport.items():
    if value == 1:
        print(key)
"""
# Poznávací značky
plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for znacky,value in plates.item():
    print(value)



