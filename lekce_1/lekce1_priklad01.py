# Příklad_Balíky:

cislobaliku = input("Zadej číslo svého balíku: ")
print(cislobaliku)

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

if baliky[cislobaliku]:
    print("Balík byl předán kurýrovi")
else:
    print("Balík nebyl předán kurýrovi")























