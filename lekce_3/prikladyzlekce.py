#Kniha
"""
class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} a stojí {self.price} Kč"

    def discount(self,amount):
        self.price -= self.price * (amount/100)

alenka = Book("Alenka", "120", "450")
print(alenka.get_info())
alenka.discount(50)
print(alenka.get_info())

#snížení knihy o za pomoci fce discount
"""
class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False
    def deliver(self):
        delivered = True

    def get_info(self):
        #neděláme is true
        if self.delivered:
          return  f'Adresa: {self.address}, Vaha: {self,weight} kg byl doručen'
        return f'Adresa: {self.address}, Vaha: {self,weight} kg nebyl doručen'


balik = Package('Brno 23', 250)
print(balik.get_info())
balik.deliver()
print(balik.get_info())


