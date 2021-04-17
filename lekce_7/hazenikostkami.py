

import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.txt")
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.txt")
import pandas
import matplotlib.pyplot as plt
kostky = pandas.read_csv("kostky.txt", header=None)
print(kostky.head())

kostky.hist(bins=[2,3,4,5,6,7,8,9,10,11,12,13])
plt.show()
