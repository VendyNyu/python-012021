# Detektivky podruhé

prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

nazevKnihy= str(input("Zadej název knihy: "))

if nazevKnihy in prodeje2019 and prodeje2020:
    celkovyProdej = prodeje2019[nazevKnihy] + prodeje2020[nazevKnihy]
    print(f"V roce 2019 a 2020 se knihy {nazevKnihy} celkem prodalo {celkovyProdej} výtisků.")
elif nazevKnihy in prodeje2020:
    print(f"V roce 2020 se knihy {nazevKnihy} prodalo {prodeje2020[nazevKnihy]} výtisků.")
else:
    print("Kniha se v letech 2019 a 2020 neprodávala.")









































"""
# Knihy se prodávala bud v roce 2019 nebo 2020 - Zkus udělat podmínku pro rok 2019 a pak následně zvlášť pro 2020, dohromady mi to nejde
operator = prodeje2019 or prodeje2020

if nazevKnihy in operator:
    print("super")
else:
    print("Žádná místnost není v této době k dispozici.")
"""



















