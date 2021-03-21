#Vakciny
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

#Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10
import pandas
ockovani = pandas.read_csv('country_vaccinations.csv')

ockovaniVybranyDen = ockovani[ockovani["date"] == "2021-03-10"]
#Vyber radku den 2021-03-10 - vsechny sloupce
print(ockovaniVybranyDen)
#pocet ockovanych v den 2021-03-10 v jednotlivých statech
print(ockovaniVybranyDen[["country","total_vaccinations"]])


#Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel
dvePodminky = ockovani[(ockovani["date"] == "2021-03-10") & (ockovani["total_vaccinations"]>1000000)]
print(dvePodminky)

#Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.
extremniHodnoty = ockovani[(ockovani["daily_vaccinations"] > 100000) | (ockovani["daily_vaccinations"] < 100)]
print(extremniHodnoty)

#Dobrovolný doplněk (ockovani["country"].isin(["United Kingdom","Finland","Italy"]))
#Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy. Použij např. funkci isin().
infoOckovani = ockovani[((ockovani["date"] == "2021-03-10") | (ockovani["date"] == "2021-03-11")) & ockovani["country"].isin(["United Kingdom","Finland","Italy"])]
print(infoOckovani)

#Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09
infoOckovaniJapan = ockovani[(ockovani["date"] >= "2021-03-03") & (ockovani["date"] <= "2021-03-09") & ockovani["country"].isin(["Japan"])]
print(infoOckovaniJapan)



