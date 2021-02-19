#Skladník

kodSoucastky = input("Zadej kód součástky: ")
print(kodSoucastky)

pocetSoucastek = int(input("Zadej počet součástek: "))
print(pocetSoucastek)

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#Všechny tři varianty z příkladu dohromady

if kodSoucastky in sklad:
    print("Součástka je skladem")
    if pocetSoucastek > sklad[kodSoucastky]:
        print("Lze prodat pouze omezené množství.")
        sklad.pop(kodSoucastky)
        # Testování - součástka byla ze seznamu odebrána:
        print(sklad)
    elif pocetSoucastek <= sklad[kodSoucastky]:
        print("Poptávku lze uspokojit v plné výši.")
        odecteniSoucastek = sklad[kodSoucastky] - pocetSoucastek
        # Testování - součástky se odečítají:
        print(f"Počet součástek na skladě: {odecteniSoucastek} ks")
else:
    print("Součástka není skladem")


"""
Poznámky (můj postup, před složením):
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
if pocetSoucastek > sklad[kodSoucastky]:
    print("Lze prodat pouze omezené množství.")
    sklad.pop(kodSoucastky)
    #Testování - součástka byla ze seznamu odebrána:
    print(sklad)
    
Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

if pocetSoucastek <= sklad[kodSoucastky]:
    print("Poptávku lze uspokojit v plné výši.")
    odecteniSoucastek = sklad[kodSoucastky] - pocetSoucastek
    #Testování - součástky se odečítají:
    print(f"Počet součástek na skladě: {odecteniSoucastek} ks")
"""
