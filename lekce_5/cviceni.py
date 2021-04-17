import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")



import pandas
jobs = pandas.read_csv("jobs.csv")
jobs.head()

#Zobrazení názvu sloupců
print(jobs.columns)

#Podívej se, kolik má soubor řádek.
jobs.shape
jobs.shape[0]

#Zjisti všechny informace o pracovní pozici na desátém řádku.
jobs.iloc[9]

#Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici

print(jobs.iloc[12:30, [1, 6]])

jobs.iloc[11:20]
jobs.columns
jobs.iloc[11:20, 6]










