# Mějme zadaný následující seznam naměřených teplot. 
# Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.


teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vytvoř seznam průměrných teplot pro každý den.
lst1 = [round(sum(teplota)/len(teplota), 2) for teplota in teploty]
print(f"Seznam prumernych teplot pro kazdy den: {lst1}")

# Vytvoř seznam ranních teplot.
lst2 = [teplota[0] for teplota in teploty]
print(f"Seznam rannich teplot: {lst2}")

# Vytvoř seznam nočních teplot.
lst3 = [teplota[-1] for teplota in teploty]
print(f"Seznam nocnich teplot: {lst3}")

# Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
lst4 = [[teplota[1], teplota[3]]for teplota in teploty]
print(f"Seznam polednich a nocnich teplot: {lst4}")


# BONUS
# Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
# {den: průměrná teplota}
temperatures = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

avrg_temps_dict = {day[0]: round(sum(day[1:])/len(day[1:]), 2) for day in temperatures}
print(avrg_temps_dict)