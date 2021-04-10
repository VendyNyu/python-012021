#Velikonoce
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

#Vytvoř sloupcový graf, který data přehledně zobrazí. Na ose x budou vidět jednotlivá data ("datumy") a výška sloupce označí, kolikrát na daný den připadly Velikonoce.

import pandas
import matplotlib.pyplot as plt
velikonoce = pandas.read_csv('velikonoce.csv')

print(velikonoce.head())
#popisky os
ax = velikonoce.plot(title = "Velikonoce", kind = "bar", color = "pink",edgecolor = "black", grid=True,legend=True, x = "Datum")
ax.set_ylabel('Počet dnů')
ax.set_xlabel('Datum')
plt.show()