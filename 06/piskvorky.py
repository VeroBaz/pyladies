#  1D piskovrky

from random import randrange

def vyhodnot(pole):
    # Vyhodnocuje hru:
    # "x" – Vyhrál hráč s křížky (pole obsahuje xxx)
    # "o" – Vyhrál hráč s kolečky (pole obsahuje ooo)
    # "!" – Remíza (pole neobsahuje -, a nikdo nevyhrál)
    # "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
    if "xxx" in pole:
        return("x")
    elif "ooo" in pole:
        return("o")
    elif "xxx" and "ooo" and "-" not in pole:
        return("!")
    else:
        return("-")

def tah(pole, policko, symbol):
    # Umistuje symbol hrace na zvolene policko v hernim poli.
    pole = "".join(list(pole)[:policko]) + symbol + "".join(list(pole)[policko + 1:])
    return pole

def tah_hrace(pole):
    # Zepta se hrace, kam chce umistit svuj symbol (overuje, ze jde o cislo od 1 do 20) a umisti jej pomoci funkce tah().
    while True:
        policko_input = input("Na kterou pozici chces umistit svuj symbol? ")
        if not policko_input.isdigit():
            print("Musis zadat cislo od 1 do 20.")
            continue
        policko = int(policko_input) - 1
        if policko not in range(20):
            print("Musis zadat cislo od 1 do 20.")
        elif list(pole)[policko] == "o" or list(pole)[policko] == "x":
            print("Policko je jiz obsazene.")
        else:
            return tah(pole, policko, symbol = "x")

def strategie_vitezstvi(pole):
    # Vybira policko pocitace tak, aby vyhral.
    if "o-o" in pole:
        policko = pole.find("o-o") + 1
        return policko
    elif "-oo" in pole:
        policko = pole.find("-oo")
        return policko
    elif "oo-" in pole:
        policko = pole.find("oo-") + 2
        return policko
    else:
        return "nic"

def strategie_obrana(pole):
    # Vybira policko pocitace tak, aby branil vitezstvi hrace.
    if "-x-" in pole:
        policko = pole.find("-x-")
        return policko
    elif "x-x" in pole:
        policko = pole.find("x-x") + 1
        return policko
    elif "xx-" in pole:
        policko = pole.find("xx-") + 2
        return policko
    elif "-xx" in pole:
        policko = pole.find("-xx")
        return policko
    else:
        return "nic"

def tah_pocitace(pole):
    # Podle strategie (funkce strategie_vitezstvi() nebo strategie_obrana()) nebo nahodne zvoli policko pocitace a umisti jej pomoci funkce tah().
    while True:
        if strategie_vitezstvi(pole) != "nic":
            policko = strategie_vitezstvi(pole)
            return tah(pole, policko, symbol = "o")
        elif strategie_obrana(pole) != "nic":
            policko = strategie_obrana(pole)
            return tah(pole, policko, symbol = "o")
        else:
            policko = randrange(0,19)
            if pole[policko] == "-":
                return tah(pole, policko, symbol = "o")

def piskvorky1d():
    # Spusti hru - vytvori herni pole, stridave umoznuje tah hrace a pocitace, dokud nekdo nevyhraje nebo neni remiza. 
    herni_pole = "--------------------"
    while vyhodnot(herni_pole) != "x" or vyhodnot(herni_pole) != "o" or vyhodnot(herni_pole) != "!":
        herni_pole = tah_hrace(herni_pole)
        print(herni_pole)
        if vyhodnot(herni_pole) == "x":
            return("Gratuluji! Vyhral jsi.")
        herni_pole = tah_pocitace(herni_pole)
        print(herni_pole)
        if vyhodnot(herni_pole) == "o":
            return("Smula. Prohral jsi.")
        if vyhodnot(herni_pole) == "!":
            return("Je to remiza.")

print(piskvorky1d())
