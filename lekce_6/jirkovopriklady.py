"""
import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
import wget

#soubory = ["https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv",
           "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv",
           "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv"]
#for soubor in soubory:
  #wget.downlo d(soubor)
"""
import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")


import  pandas
u202 = pandas.read_csv('u202.csv')

print(u202.head())
print(u202["znamka"].isnull())

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
#chci si spojit všechny tabulky do jedné vytvoří novou tabulka - maturita

maturita = pandas.concat([u202, u203,u302], ignore_index=True)
print(maturita.head())
maturita.to_csv("maturita.csv", index=False)

studenti = pandas.read_csv("studenti.csv")
predsedajici = pandas.read_csv("predsedajici.csv")


#Spojení dvou tabulek
vysledky_se_jmeny = pandas.merge(maturita,studenti, how="left")
print(vysledky_se_jmeny.head())
print(maturita.shape)
print(studenti.shape)

#chci vědět, kde jsou prázdné řádky
print(vysledky_se_jmeny[vysledky_se_jmeny['jmeno'].isnull()])
#řádek je podezřelý není tam kdo měl tyto výsledky

print(u202.shape)

vysledky_se_jmeny = pandas.merge(u202, studenti, how="left")

vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on = "den")
print(vysledky_se_jmeny_a_predsedajicimi)








