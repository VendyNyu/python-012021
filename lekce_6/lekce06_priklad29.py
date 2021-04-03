#Státy světa potřetí

import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv('temperature.csv')

#Zkopírované z mého příkladu 25, přidání sloupce se stupněm C
import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])
#print(temperature)
#Vytvořen nový sloupec AvgTemperatureCelsia

#Vyfiltruj si informace o teplotách 13. listopadu 2017
info_teplota = temperature[temperature["Day"] == 13]
print(info_teplota)

#Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
chybny_zaznam = temperature[temperature["AvgTemperatureCelsia"] != -99]
print(chybny_zaznam)

#Vypočti počet dat, které máš pro daný den za jednotlivé regiony
print(temperature.groupby("Region").count())

#Vypočti průměrnou teplotu za jednotlivé regiony
print(temperature.groupby("Region").mean())

#Vypočti maximální a minimální teplotu v každém regionu
#maximální
print(temperature.groupby("Region").max())
#minimální
print(temperature.groupby("Region").min())

