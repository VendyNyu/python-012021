#Klíč k úspechu


#Body a kritéria

odvetvi = input("Zadej odvětví firmy: ")

def getCriteriaPoints(odvetvi = True, obrat = True, stat = True, konference = False, newsletter = False):
    if odvetvi == "automotive":
        body = 3
        obrat = int(input("Zadej obrat v eurech: "))
        if obrat < 10000000:
            body = 3
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body +=0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0

            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0

        elif 10000000 <= obrat <= 1000000000:
            body += 3
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0

        else:
            body += 1
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0

    elif odvetvi == "retail":
        body = 2
        obrat = int(input("Zadej obrat v eurech: "))
        if obrat < 10000000:
            body = 2
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
        elif 10000000 <= obrat <= 1000000000:
            body += 3
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
        else:
            body += 1
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
    else:
        body = 0
        obrat = int(input("Zadej obrat v eurech: "))
        if obrat < 10000000:
            body = 0
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
        elif 10000000 <= obrat <= 1000000000:
            body += 3
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
        else:
            body += 1
            stat = input("Zadej stát ve které má firma sídlo: ")
            if stat == "Česká republika" or stat == "Slovensko":
                body += 2
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            elif stat == "Německo" or stat == "Francie":
                body += 1
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
            else:
                body += 0
                konference = input("Účastnil se zákazník konference v loňském roce? ")
                if konference == "ano":
                    body += 1
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
                else:
                    body += 0
                    newsletter = input("Odebírá firma newsletter? ")
                    if newsletter == "ano":
                        body += 1
                    else:
                        body += 0
    return body
print(getCriteriaPoints(odvetvi))

if getCriteriaPoints(odvetvi)<=5:
    print("Šance na získání je malá.")
elif 6<=getCriteriaPoints(odvetvi)<=8:
    print("Šance na získání je střední.")
else:
    print("Šance na získání je vysoká.")

#getCriteriaPoints(odvetvi)