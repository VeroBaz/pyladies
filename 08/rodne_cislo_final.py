# Tento program overuje, zda uzivatel zadal spravne rodne cislo

def spravny_format(rodne_cislo):
    try:
        rodne_cislo_11 = int(rodne_cislo[0:6] + rodne_cislo[7:10]) % 11 == int(rodne_cislo[10])
        if rodne_cislo_11:
            return "Zadal/a jste spravne rodne cislo."
        else:
            return "Zadal/a jste spatne rodne cislo."
    except ValueError:
        return "Zadal/a jste spatne rodne cislo."
    except IndexError:
        return "Zadal/a jste spatne rodne cislo."

rodne_cislo = input("Napis rodne cislo: ")
print(spravny_format(rodne_cislo))