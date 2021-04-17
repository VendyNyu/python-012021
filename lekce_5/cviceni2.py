import pandas
jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")
#---------
jmena.loc["Jiří"]
From Kristýna Sodomková to Everyone:  08:14 PM
jop, už to funguje
From Aleš Hura (kouč) to Everyone:  08:20 PM
jmena.loc[["Martin", "Zuzana", "Josef"]]
#3----------
jmena.loc[:"Martin"]
#4------------
jmena.loc["Martin":"Tereza", "věk"]
-----------------
#1-------------
jmena[jmena["věk"] > 60]

import pandas
jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")
#2----------2
jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)]

vybranaJmena = jmena[[jmena["původ"].isin([["slovanský", "hebrejský"])]
vybranaJmena[["jméno", "četnost"]]


vybranaJmena.shape
vybranaJmena = jmena[jmena["svátek"].isin(["1.2.", "2.2.", "3.2." ])]
