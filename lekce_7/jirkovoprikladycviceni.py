import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

import pandas

staty = pandas.read_json("staty.json")

staty = staty.set_index("name")

staty["population_density"] = staty["population"] / staty["area"]
#v závorce podle čeho to řadím (False - sestupný řazení? )
staty= staty.sort_values("population_density", ascending=False)
print(staty.head())