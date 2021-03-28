#Projekty
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

#Načti data ze souboru a ulož je do tabulky
import pandas
projekty = pandas.read_csv('vykazy.csv')

#Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
serazeni_projekty = projekty.groupby('project')['hours'].count()
print(serazeni_projekty)



