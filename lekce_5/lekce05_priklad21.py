import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
twlo = pandas.read_csv('twlo.csv')

#Kolik má soubor twlo.csv řádek a kolik sloupců:
poceRadekSloupcu = twlo.shape
print(poceRadekSloupcu)

#Zjištění nejnovější ceny akcie (tedy zobrazení posledního řádku):
print(twlo.iloc[-1:])

#5 řádků s cenami na začátku souboru (tedy řádek 0 až 4):

#Zobrazení pomocí iloc:
print(twlo.iloc[:5])

#Zobrazení pomoci head:
print(twlo.head())

#Dobrovolný doplněk:
#Pocet radku uloz do promenne pocet radku jako cislo
pocet_radku = int(twlo.shape[0])
print(f'počet řádků: {pocet_radku}')
#Načtení první hodnoty zavírací doby (sloupec Close) a poslední hodnoty zavírací ceny v souboru
prvni_hodnota = twlo.iloc[0,[5]]
#print(twlo.iloc[0,[5]])
druha_hodnota = twlo.iloc[-1,[5]]
#print(twlo.iloc[-1,[5]])

#Vypočítej, o kolik procent se zvýšila hodnota akcie
vypocet = ((druha_hodnota/prvni_hodnota) * 100)-100
print(vypocet)

#Maximální zaznamenaná cena v sloupci High
print(twlo.iloc[:,[3]].max())
#Minimální zazanamená cena ve sloupci Low
print(twlo.iloc[:,[4]].min())



