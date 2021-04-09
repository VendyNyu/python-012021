import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv('temperature.csv')

#Zkopírované z mého příkladu 25, přidání sloupce se stupněm C
import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])
#print(temperature)
#Vytvořen nový sloupec AvgTemperatureCelsia

#Vyfiltruj si informace o teplotách 13. listopadu 2017.
info_teplota = temperature[temperature["Day"] == 13]
print(info_teplota)

#Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
chybny_zaznam = temperature[temperature["AvgTemperatureCelsia"] != -99]
print(chybny_zaznam)

#Dva příklady výše se shodují s body v příkladu 29 - pouze zkopírované, zeptat se na to

#Seřad hodnoty v souboru podle teploty od největší po nejmenší.
#řazení - sort_values s SQL - order by
#řazení sestupně - od největšího po nejmenší (ascending = False)
print(chybny_zaznam.sort_values(by='AvgTemperatureCelsia',ascending=False))

#Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.

#Nejvyšší
nejvyssi = temperature.groupby("Region").max().head()
print(nejvyssi)
#prvních 5 hodnot seřazených vzestupně
print(nejvyssi.sort_values(by='AvgTemperatureCelsia'))

#Nejmenší
nejnizsi = temperature.groupby("Region").min().head()
print(nejnizsi)
#prvních 5 hodnot seřazených vzestupně
print(nejnizsi.sort_values(by='AvgTemperatureCelsia'))