#Zaměstnanci
"""
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
"""

#Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje

import pandas
zam_liberec = pandas.read_csv('zam_liberec.csv')
zam_plzen = pandas.read_csv('zam_plzeň.csv')
zam_praha = pandas.read_csv('zam_praha.csv')
platy2021 = pandas.read_csv('platy_2021_02.csv')

zam_liberec['mesto'] = 'Liberec'
zam_plzen['mesto'] = 'Plzeň'
zam_praha['mesto'] = 'Praha'

#Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
zamestnanci = pandas.concat([zam_praha, zam_liberec, zam_plzen],ignore_index=True)

print(zamestnanci)

#Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.

zamestnanci_s_platy = pandas.merge(zamestnanci,platy2021, on=['cislo_zamestnance'])
print(zamestnanci_s_platy)
zamestnanci_s_platy.to_csv('zamestnanci_s_platy',index=False)

#Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.

#rozměr tabulek před spojením
print(zamestnanci.shape)
print(platy2021.shape)
#rozměr tabulky po spojení
print(zamestnanci_s_platy.shape)
#Byly porovnány rozměry, dle čísel nemá plat za únor 13 zaměsntanců (tito zaměstnanci ve firmě zřejmě již nepracují)

#Průměrný plat zaměstnanců v jednotlivých kancelářích:
print(zamestnanci_s_platy.groupby("mesto")["plat"].mean())

#Dobrovolný doplněk
#Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
#Pokud zamestnanci chybi plat, znamená to, že ve společnosti již nepracuje
novymerge = pandas.merge(zamestnanci,platy2021, on=['cislo_zamestnance'], how="outer")
print(novymerge)
print(f"Kolik zaměstnanců v únoru ve společnosti již nepracuje: {sum(novymerge['plat'].isnull())}")

#V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
odesli_zamestnanci = novymerge[novymerge["plat"].isnull()]
print(odesli_zamestnanci)
#uložení do CSV
odesli_zamestnanci.to_csv('odesli_zamestnanci',index=False)
