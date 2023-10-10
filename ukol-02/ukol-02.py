# Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. 

#Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. 

# Obě informace si ulož. Následně naprogramuj následující varianty:

# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.

# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.

# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print("Dobry den!")
y_or_n = input("Chcete u nas nakoupit? Napis Y or N: ").strip().upper()

while y_or_n == "Y":
    
    soucastka = input("Jakou soucastku si chcete koupit? ").strip().upper()

    if soucastka in sklad:

        pocet = int(input("Kolik kusu budete chtit? ").strip())

        if pocet < sklad[soucastka]:
            print(f"Mame dostatek kusu. Prodam vam {pocet} soucastek.")
            sklad[soucastka] -= pocet

        elif pocet == sklad[soucastka]:
            print(f"Mame dostatek kusu. Prodam vam {pocet} soucastek.")
            sklad.pop(soucastka)

        elif pocet > sklad[soucastka]:
            print(f"Na sklade je mene kusu nez pozadujete. Lze prodat pouze {sklad[soucastka]} kusu.")
            ks = input(f"Koupite si tyto soucastky? Napis Y or N: ").strip().upper()
            if ks == "Y":
                print(f"Prodam vam {sklad[soucastka]} kusu soucastek.")
                sklad.pop(soucastka)

    else:
        print("Soucastka neni skladem.")
  
    y_or_n = input("Budete si prat neco dalsiho? Napis Y or N: ").strip().upper()

print("Nashledanou")

