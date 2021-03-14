from forex_python.converter import CurrencyRates
menaProSmenu = input("Zadejte měnu, kterou chcete směnit: ")
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadejte požadované množství měny: "))
cena_v_korunach = prevodnik.convert(menaProSmenu, 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)
