from django.db import models

# Create your models here.
#Příklad 42 Auto:
class Auto(models.Model):
 registracni_znacka = models.CharField(max_length=100)
 znacka_typ = models.CharField(max_length=100)
 pocet_najetych_km = models.IntegerField()
 datum_tech_kontroly = models.DateField()

#Příklad 44 Zákazník:
class Zakaznik(models.Model):
 jmeno_prijmeni =  models.CharField(max_length=100)
 cislo_ridicskeho_prukazu = models.CharField(max_length=100)
 datum_narozeni = models.DateField()

#Příklad 45 Výpůjčka:
class Vypujcka(models.Model):
 datum_cas_zacatku_vypujcky = models.DateTimeField()
 datum_cas_konce_vypujcky = models.DateTimeField()
 cena_vypujcky = models.IntegerField()