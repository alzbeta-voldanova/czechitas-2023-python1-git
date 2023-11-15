class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
        
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji zapujceni vozidla."
        else:
            return "Vozidlo neni k dispozici."
    
    def get_info(self):
        return f"{self.registracni_znacka} {self.typ_vozidla}"

    def vrat_auto(self, stav_tachometru, dny_zapujceni):
        self.najete_km = stav_tachometru
        self.dostupne = True
        if dny_zapujceni < 7:
            return f"Cena za pujceni auta: {dny_zapujceni * 400} Kc."
        else:
            return f"Cena za pujceni auta: {dny_zapujceni * 300} Kc."
    
    def pocet_km(self):
        return self.najete_km
    
    def pujcene_auto(self):
        return self.dostupne


auto_1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto_2 = Auto("1P3 4747", "Škoda Octavia", 41253)


pujcit_vratit = True
while pujcit_vratit:
    print("***   pujcit auto: A, vratit auto: B, rozloucit se: C   ***")
    sluzba = input("Napiste pismeno sluzby o kterou mate zajem: ").upper().strip()
    
    if sluzba == "A":
        print("Peugeot: 1, Skoda: 2")
        znacka_auta = input("Jakou znacku auta vyberete? Napiste jeji cislo: ").strip()
        if znacka_auta == "1":
            print(auto_1.get_info())
            print(auto_1.pujc_auto())
            print(" ")
        elif znacka_auta == "2":
            print(auto_2.get_info())
            print(auto_2.pujc_auto())
            print(" ")
        else:
            print("Takovou znacku auta nemame.")
            print(" ")
            continue
    
    elif sluzba == "B":
        znacka_auta = input("Jakou znacku auta vracite? Napiste cislo (Peugeot: 1, Skoda: 2): ")
        if znacka_auta == "1" and auto_1.pujcene_auto() == False:
            tachometr = int(input(f"Pri pujceni melo auto najeto {auto_1.pocet_km()} km. Kolik je na tachometru nyni? "))
            dny = int(input("Kolik dni jste mel auto zapujcene? "))
            print(auto_1.vrat_auto(tachometr, dny))

        elif znacka_auta == "2" and auto_2.pujcene_auto() == False:
            tachometr = int(input(f"Pri pujceni melo auto najeto {auto_2.pocet_km()} km. Kolik je na tachometru nyni? "))
            dny = int(input("Kolik dni jste mel auto zapujcene? "))
            print(auto_2.vrat_auto(tachometr, dny))

        else:
            print("Takove auto nemame v evidenci na vraceni. Nespletl jste si pujcovnu?")
            print(" ")
            continue
    
    elif sluzba == "C":
        print("Nashledanou")
        pujcit_vratit = False

    else:
        continue



