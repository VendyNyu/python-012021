#Státy světa potřetí
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
import pandas
staty = pandas.read_json('staty.json')
gdp = pandas.read_csv('gdp.csv')


#Vyfiltruj státy, které leží v Evropě

staty_v_Evrope = staty[staty["region"] == "Europe"]
print(staty_v_Evrope)

#Zjisti počet států v jednotlivých subregionech
pocet_statu_v_subregionech = staty.groupby('subregion')['name'].count()
print(pocet_statu_v_subregionech)

#Zjisti celkový počet obyvatel v jednotlivých subregionech Evropy
pocet_populace_v_subregionech = staty.groupby('subregion')['population'].sum()
print(pocet_populace_v_subregionech)

#Rozšířené zadání
#Z tabulky s GDP odeber státy, které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
odebrane_staty_s_chybejicim_GDP = gdp.dropna()
print(odebrane_staty_s_chybejicim_GDP)





