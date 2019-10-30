# Tento program:
# 1) overuje, zda uzivatel zadal rodne cislo ve spravnem formatu (123456/7899)
# 2) overuje, zda jej zadal bez chyby (prvnich devet cisel modulo 11 se rovna poslednimu cislu)
# 3) vypise uzivatelovo datum narozeni
# 4) vypise, zda je uzivatel muz nebo zena

from sys import exit

# Rodne cislo je ve správném formátu: 6 číslic, lomítko, 4 číslice?

def spravny_format(rodne_cislo):
    if rodne_cislo[0:6].isdigit() and rodne_cislo[7:11].isdigit() and rodne_cislo[6] == "/":
        return("Zadal/a jste rodne cislo ve spravnem formatu.")
    else:
        return exit("Zadal/a jste rodne cislo ve spatnem formatu.")

# Prvnich devet cisel deleno jedenacti rovna se posledni cislo?

def delitelne_jedenacti(rodne_cislo):
    rodne_cislo_11 = int(rodne_cislo[0:6] + rodne_cislo[7:10]) % 11 == int(rodne_cislo[10])
    if rodne_cislo_11:
        return("Zadal/a jste rodne cislo bez chyby.")
    else:
        return exit("Zadal/a jste rodne cislo s chybou.")

# Jaké datum narození je v čísle zakódováno? (vypíše trojici čísel – den, měsíc, rok)

def datum_narozeni(rodne_cislo):
    # den
    day = rodne_cislo[4:6]
    # mesic
    if rodne_cislo[2:4] in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        month = rodne_cislo[2:4]
    else:
        month = str(int(rodne_cislo[2]) - 5) + rodne_cislo[3]
    # rok
    if int(rodne_cislo[0:2]) > 19:
        year = f"19{rodne_cislo[0:2]}"
    else:
        year = f"20{rodne_cislo[0:2]}"
    # datum narozeni
    return(f"Vase datum narozeni je {day}. {month}. {year}.")

# Jaké pohlaví je v čísle zakódováno? (vypíše 'muž' nebo 'žena')

def muz_zena(rodne_cislo):
    if rodne_cislo[2:4] in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        return("Jste muz.")
    else:
        return("Jste zena.")

rodne_cislo = input("Napis rodne cislo: ")
print(spravny_format(rodne_cislo))
print(delitelne_jedenacti(rodne_cislo))
print(datum_narozeni(rodne_cislo))
print(muz_zena(rodne_cislo))
