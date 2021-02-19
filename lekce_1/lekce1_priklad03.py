#Zasedačky

hodina = int(input("V kolik hodin chcete zamluvit meeting room? "))

volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}


if hodina in volnePokoje:
    print(f"Počet volných místností: {len(volnePokoje[hodina])}")
    print(f"Volné jsou tyto místnosti: {volnePokoje[hodina]}")
else:
    print("Žádná místnost není v této době k dispozici.")


"""    
#Počet volných místností:

print(f"Počet volných místností: {len(mistnosti)}")


# Seznam místností, které jsou volné:
print(f"Volné jsou tyto místnosti: {mistnosti}")
"""










