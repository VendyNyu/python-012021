print("Instrukce pro uživatele: Zadejte údaje do jednotlivých polí. U otázky číslo 1,4,5 zadejte údaj malým písmenem. U otázky číslo 2 zadejte číslo bez mezer. Stát u otázky číslo 3 musí začít velkým písmenem. Děkujeme.  ")

odvetvi = input("1. Zadej odvětví firmy: ")
obrat = int(input("2. Zadej obrat v eurech: "))
stat = input("3. Zadej stát ve které má firma sídlo: ")
konference = input("4. Účastnil se zákazník konference v loňském roce? ")
newsletter = input("5. Odebírá firma newsletter? ")

def getCriteriaPoints(odvetvi, obrat , stat, konference = False, newsletter = False):
    point = 0
    if odvetvi == "automotive":
        point += 3
    elif odvetvi == "retail":
        point += 2
    else:
        point += 0

    if obrat < 10000000:
        point += 0
    elif 10000000 <= obrat <= 1000000000:
        point += 3
    else:
        point += 1

    if stat == "Česká repubilka " or stat == "Slovensko":
        point += 2
    elif stat == "Německo" or stat == "Francie":
        point += 1
    else:
        point += 0

    if konference == "ano":
        konference= True
        point += 1
    else:
        konference = False
        point += 0

    if newsletter == "ano":
        newsletter = True
        point += 1
    else:
        konference = False
        point +=0

    if point <= 5:
        return "nízkou šanci"
    elif point <= 8:
        return "střední šanci"
    else:
        return "vysokou šanci"


sance = getCriteriaPoints(odvetvi,obrat,stat,konference,newsletter)

print(f" Zakázka má {sance} na úspěch.")
