#Pokročila varianta prikladu 24
"""
Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia. Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.
"""
import pandas
teplota = pandas.read_csv('temperature.csv')
import pytemperature
#Vložení sloupce navíc
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
print(teplota)

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia
vyssiTeplota = teplota[teplota["AvgTemperatureCelsia"] > 30]
print(vyssiTeplota)

#Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe)
vyssiTeplotaRegion = teplota[(teplota["AvgTemperatureCelsia"] > 15) & teplota["Region"].isin(["Europe"])]
print(vyssiTeplotaRegion)

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů
extremniHodnoty = teplota[(teplota["AvgTemperatureCelsia"] > 30) | (teplota["AvgTemperatureCelsia"] < -10)]
print(extremniHodnoty)

#Např. řádky 168-215 jsou podezřelé. Region je zde uveden Afrika a stupňů Celsia -72.78


