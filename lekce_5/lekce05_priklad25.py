#Teplota ve městech podruhé
import pandas
teplota = pandas.read_csv('temperature.csv')
import pytemperature
#Vložení sloupce navíc
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
#print(teplota)

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia
vyssiTeplota = teplota[teplota["AvgTemperatureCelsia"] > 30]
#print(vyssiTeplota)

#Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe)
vyssiTeplotaRegion = teplota[(teplota["AvgTemperatureCelsia"] > 15) & teplota["Region"].isin(["Europe"])]
#print(vyssiTeplotaRegion)

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů
extremniHodnoty = teplota[(teplota["AvgTemperatureCelsia"] > 30) | (teplota["AvgTemperatureCelsia"] < -10)]
#print(extremniHodnoty)


#Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13)
listopad = teplota[(teplota["Day"] == 13)]
print(listopad)

#Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US)
spojeneStatyAmericke = teplota[(teplota["Day"] == 13) & teplota["Country"].isin(["US"])]
print(spojeneStatyAmericke)

#Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia
mesta = spojeneStatyAmericke[spojeneStatyAmericke["City"].isin(["Washington","Philadelphia"])]
print(mesta)

#Dobrovolný doplněk
#Průměrná hodnota
prumer = spojeneStatyAmericke["AvgTemperatureCelsia"].mean()
print(prumer)
#Medián
median = spojeneStatyAmericke["AvgTemperatureCelsia"].median()
print(median)
#Rozptyl
rozptyl = spojeneStatyAmericke["AvgTemperatureCelsia"].var()
print(rozptyl)