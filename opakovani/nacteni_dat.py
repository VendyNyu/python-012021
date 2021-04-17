#Nabídky práce
#Načti data do DataFrame, který si pojmenuj jobs.
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")

import pandas
projekty = pandas.read_csv('jobs.csv')

#Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.

print(projekty.columns)

#Podívej se, kolik má soubor řádek
print(projekty.shape[0])

#Zjisti všechny informace o pracovní pozici na desátém řádku.
print(projekty.loc[10])

#Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.
print(projekty.iloc[12:21])