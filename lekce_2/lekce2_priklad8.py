#SMS brána

#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát. FUNGUJE TESTOVÁNO
telNumber = input("Zadej telefonní číslo příjemce: ")

spaceTel = telNumber.replace(" ","")
def getTelNumber(telSymbol = len(spaceTel)):
    if telSymbol == 9:
        validity = True
        #Telefonní číslo je platné
    elif telSymbol == 13 and telNumber[0:4] == "+420":
        validity = True
        #Telefonní číslo je platné
    else:
        validity = False
        #Telefonní číslo není platné
    return validity
#getTelNumber()

import math

if getTelNumber():
    print("Telefonní číslo je platné.")
    smstext = input("Zpráva: ")


    def getPriceSms(smsSymbol=len(smstext)):
        if smsSymbol <= 180:
            price = 3
            print(f"Cena tvé sms je {price} Kč")
        else:
            smsNumber = smsSymbol / 180
            roundedup = math.ceil(smsNumber)
            price = roundedup * 3
            print(f"Cena tvé sms je {price} Kč")

        return price

    getPriceSms()
else:
    print("Chyba, zadané číslo je neplatné.")



"""
Můj postup, kód napsaný zvlášť: 
A)
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát. KOD FUNGUJE, TESTOVÁN
telNumber = input("Zadej telefonní číslo příjemce: ")

spaceTel = telNumber.replace(" ","")
def getTelNumber(telSymbol = len(spaceTel)):
    if telSymbol == 9:
        validity = True
        print("Telefonní číslo je platné.")
    elif telSymbol == 13 and telNumber[0:4] == "+420":
        validity = True
        print("Telefonní číslo je platné.")
    else:
        validity = False
        print("Chyba, zadané číslo je neplatné!")
    return validity
getTelNumber()


B)
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát. KOD FUNGUJE, TESTOVÁN 
import math
smstext = input("Zpráva: ")

def getPriceSms(smsSymbol = len(smstext)):
    if smsSymbol <= 180:
        price = 3
        print(f"Cena tvé sms je {price} Kč")
    else:
        smsNumber = smsSymbol/180
        roundedup = math.ceil(smsNumber)
        price = roundedup * 3
        print(f"Cena tvé sms je {price} Kč")

    return price
getPriceSms()
"""












