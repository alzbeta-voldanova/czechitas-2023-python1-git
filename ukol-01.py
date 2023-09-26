# UKOL-01
# Napiš program, který bude obsahovat jednu proměnnou jmeno. 
# Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). 
# Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.

# Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz.

jmeno = "Alexandr"

def create_email(name):
    email = f"{name}@czechitas.cz"
    return email


print(create_email(jmeno))


# BONUS
# Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. 
# Obsah proměnné načti od uživatele pomocí funkce input. 
# Tvůj program postupně vypíše několik způsobů formátování jména:

    # všechna písmena velká (vypíše např. JANA MALÁ)
    # všechna písmena malá (vypíše např. jana malá)
    # standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
    # iniciály (vypíše např. J. M.)
    # křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, 
        # tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
# Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?).


jmeno_a_prijmeni = input("Zadej jmeno a prijmeni: ").lower()


def all_letters_upper(name):
    return name.upper()

def all_letters_lower(name):
    return name.lower()

def capitalized(name):
    lst_of_names = name.split()
    capitalized_name = ""
    for nm in lst_of_names:
        capitalized_name = capitalized_name + nm.capitalize() + " "
    return capitalized_name.strip()

def initials(name):
    lst_of_names = name.split()
    initials = ""
    for nm in lst_of_names:
        initials = initials + nm[0].upper() + ". "
    return initials.strip()
    
def not_too_long_name(name):
    # create list from input name which consists of parts of the full name according to the rules
    lst_of_names = name.split()
    names = []
    for nm in lst_of_names:
        if (len(nm) > 5) and (lst_of_names.index(nm) < (len(lst_of_names) - 1)):
            names.append(nm[0].upper() + ".")
        else:
            names.append(nm.capitalize()) 
    # concatenate the parts of the full name to the final string 
    final_name = ""
    for nm in names:
        final_name = final_name + nm + " "
    return final_name.strip()


print(all_letters_upper(jmeno_a_prijmeni))
print(all_letters_lower(jmeno_a_prijmeni))
print(capitalized(jmeno_a_prijmeni))
print(initials(jmeno_a_prijmeni))
print(not_too_long_name(jmeno_a_prijmeni))


# test:
    # Alzbeta Voldanova
    # Elis Voldanova
    # ALZBETA VOLDANOVA
    # Elis Emilie Voldanova
    # Elis Emma Alzbeta Voldanova
    # Alzbeta Elis Emilie Anet Heck
    # Voldanova

