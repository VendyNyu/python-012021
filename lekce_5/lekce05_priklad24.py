#Teplota ve městech
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teplota = pandas.read_csv('temperature.csv')

#Vypsání prvních několika řádků pro prohlídnutí struktury tabulky
print(teplota.head())

#Dotaz na měření, která byla provedena v Praze
mereniPraha = teplota[teplota["City"].isin(["Prague"])]
print(mereniPraha)
#v tabulce je průměrná teplota uváděná nikoli ve stupních celsia, ale Fahrenheita

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů
vyssiTeplota = teplota[teplota["AvgTemperature"] > 80]
print(vyssiTeplota)

#Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe
vyssiTeplotaRegion = teplota[(teplota["AvgTemperature"] > 60) & teplota["Region"].isin(["Europe"])]
print(vyssiTeplotaRegion)

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů
extremniHodnoty = teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)]
print(extremniHodnoty)
