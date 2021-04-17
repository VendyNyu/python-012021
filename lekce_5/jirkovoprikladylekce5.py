
import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
nakupy = pandas.read_csv('nakupy.csv')

#Chci první tři řádky [0:3], poslední tři řádky [-3:]

#print(nakupy.iloc[-3:])

"""
print(nakupy.head(n=3))
print(nakupy.tail(n=2))
"""

#vypsání sloupců [řádek, sloupec] - [0,3] - znamená vypiš sloupce 0 a 3
print(nakupy.head(n=3))
print(nakupy.iloc[:,[0,3]])
