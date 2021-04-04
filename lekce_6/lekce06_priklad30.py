#Eport do Excelu
import pandas
import openpyxl
#Uložení do excelu

vykazy = pandas.read_csv('vykazy.csv')
serazeni_projekty = vykazy.groupby('project')['hours'].sum()
#pozor excel přípona xlsx
#vykazy_excel = serazeni_projekty.to_excel('vykazy.xlsx')

nacteni_excel = pandas.read_excel('vykazy.xlsx')
print(nacteni_excel)



