#Hra o trůny
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

#Nastevení sloupce Name jako index (použiji fci set_index()):
import pandas
deaths = pandas.read_csv('character-deaths.csv')
deaths = deaths.set_index('Name')
#print(deaths.index)

#Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
#nazvy sloupců:
print(deaths.columns)
#sloupce a informace v nich:
print(deaths.iloc[:])


#Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali"
print(deaths.loc['Hali'])

#Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
print(deaths.loc['Gevin Harlaw':'Gillam'])

#Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year
print(deaths.loc[['Gevin Harlaw','Ghael','Ghost of High Heart','Gillam'],['Death Year']])

#Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD
print(deaths.loc[['Gevin Harlaw','Ghael','Ghost of High Heart','Gillam'],['GoT','CoK','SoS','FfC','DwD']])




