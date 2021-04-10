#Histogram platů
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
import pandas
import matplotlib.pyplot as plt
platy = pandas.read_csv('platy_2021_02.csv')
#Seřazení tabulky vzestupně
platy = platy.set_index('cislo_zamestnance')
print(platy.head())

#Stanovení hranice v hystogramu v bins
graf = platy.hist(bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000], color = "pink", grid=True, legend=True)


#Zobrazení histogramu
plt.show()

