import sys

rodne_cislo = input("Napis rodne cislo: ")

# Obashuje rodne cislo cisla?
jen_cisla = rodne_cislo[0:6] + rodne_cislo[7:11]
if not jen_cisla.isdigit():
    sys.exit("Zadal jste spatne rodne cislo.")

# Ma rodne cislo spravnou delku?
spravna_delka = len(rodne_cislo) == 11
if not spravna_delka and "/" in rodne_cislo:
    sys.exit("Zadal jste rodne cislo ve spatne delce.")

# Je rodne cislo ve správném formátu: 6 číslic, lomítko, 4 číslice?
spravny_format = rodne_cislo[0:6].isdigit() and rodne_cislo[7:11].isdigit() and rodne_cislo[6] == "/"
if not spravny_format:
    sys.exit("Zadal jste rodne cislo ve spatnem formatu.")

# Prvnich devet cisel deleno jedenacti rovna se posledni cislo?
delitelne_jedenacti = int(rodne_cislo[0:6] + rodne_cislo[7:10]) % 11 == int(rodne_cislo[10])
if not delitelne_jedenacti:
    sys.exit("Zadal jste rodne cislo s chybou.")

# Vypise, ze rodne cislo je spravne.
else:
    print("Zadal jste spravne rodne cislo.")