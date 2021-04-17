from datetime import datetime,timedelta


soucasne_datum = datetime.now()

print(soucasne_datum.strftime("%d.%m.%Y, %H:%M"))


#Cvičeni kodim.cz
#Převod času
apolloStart = datetime(1969, 7, 16, 14, 32)
print(apolloStart.strftime("%m/%d/%Y"))

#Čas od startu
start = datetime(2020,2,10)

#Jaký byl den?
print(f"Jaký byl den: {start.weekday()}")
#weekday začíná od 0 tudíž bylo pondělí
utekly_cas = soucasne_datum - apolloStart
print(utekly_cas)

#Doprava večeře
objednavka = datetime(2020,11,13,19,47)
prevzeti = timedelta(minutes=8,seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25,seconds=30)
print(objednavka+prevzeti+priprava+doprava)


