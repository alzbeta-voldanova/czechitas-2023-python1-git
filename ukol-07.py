#1
# Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:

# platná data:
# 2.2.2022
# 13. 8. 1999
# 4/5/2001

# neplatná data:
# 5.123.458.91
# 21.4
# 8./9

regularni_vyraz_1 = r"\d?\d(.|/) ?\d(.|/) ?\d{4}"



#2
# Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18.

regularni_vyraz_2 = r"\d{3} \d{2} {1,3}[A-Ž ]+\d*"


