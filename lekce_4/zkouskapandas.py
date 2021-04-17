"""
import wget
wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
"""
import pandas
nakupy = pandas.read_csv('nakupy.csv')
#info ohledně toho - nerozumím
nakupy.info()
#vypíše mi celou tabulka
print(nakupy)
#vypíše mi počet sloupců a řádků
print(nakupy.shape)
#vypíše mi název sloupců
print(nakupy.columns)

#jak vybra jeden nákup
print(nakupy.iloc[3])
