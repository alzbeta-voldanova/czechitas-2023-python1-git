# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
    # Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
    # Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:
    # První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
    # Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
# Tipy:
# Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
# Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

import math

def check_symbols(number):
    # odstrani mezery
    ok_number = number.replace(" ", "")

    # zkontroluje a odstrani  predvolbu
    if ok_number[:4] == '+420':
        ok_number = ok_number[4:]
    
    # zkontroluje spravnou delku
    if len(ok_number) != 9:
        return False
    
    # zkontroluje, zda cislo obsahuje pouze cislice
    nums =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in ok_number:
        if num in nums:
            continue
        else:
            return False
    return True


def message_price(message):
    length = len(message)
    if length == 0:
        return 3
    else:
        price = math.ceil(length / 180) * 3
        return price
    


try_it_again = True
while try_it_again:
    phone_number = input("Enter recipient phone number: ")
    correct_number = check_symbols(phone_number)
    
    if correct_number:
        message = input("Write the message: ")
        print(f"Message price: {message_price(message)} Kc")
        again = input("Do you want to send another message? Type Y or N: ").upper().strip()
        if again == "Y":
            try_it_again = True
        else:
            try_it_again = False

    else:
        print("The phone number is wrong written.")
        again = input("Do you want to enter it again? Type Y or N: ").upper().strip()
        if again == "Y":
            try_it_again = True
        else:
            try_it_again = False



# TEST func check_symbols
# print(check_symbols('+4209aaaaaaaa'))
    # +420123456789 -> True
    # +420 123 456 789 -> True
    # 123456789 -> True
    # 123 456 789 -> True
    # 123 456 7 -> False
    # +421123456789 -> False
    # +42012345 -> False
    # +42112345678910 -> False
    # +4209aaaaaaaa -> False