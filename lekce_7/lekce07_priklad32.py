#Twilio podruhé

import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")

#Výše uvedeným programem načti data o vývoji ceny akcie. Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.
#Graf1
graf1 = twilio.plot("Date","Close", color="black")
graf1.set_title("Graf1:Vývoj ceny akcie")
graf1.set_ylabel("Cena")
graf1.set_xlabel("Datum")
plt.show()
#Graf2
twilio["Date"] = pandas.to_datetime(twilio["Date"])
graf2 = twilio.plot("Date","Close", color="green")
graf2.set_title("Graf2:Vývoj ceny akcie")
graf2.set_ylabel("Cena")
graf2.set_xlabel("Datum")
plt.show()
#Rozdíl na ose X v zobrazení data

