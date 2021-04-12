#Teplota ve městech popáté
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
import matplotlib.pyplot as plt
temperature = pandas.read_csv('temperature.csv')

#Zkopírované z mého příkladu 25, přidání sloupce se stupněm C
import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

#Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo
city_temperature = temperature[(temperature["City"] == "Helsinki") | (temperature["City"] == "Miami Beach") | (temperature["City"] == "Tokyo")]

print(city_temperature)

#Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech
graf = city_temperature.boxplot(column = "AvgTemperatureCelsia",by="City",color = "red")
graf.set_title("Porovnánní měst")
graf.set_ylabel("Teplota")
graf.set_xlabel("Město")
plt.show()

