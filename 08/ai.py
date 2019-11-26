# Cast hry piskorky - tah pocitace, strategie pocitace

from random import randrange
import util

def tah_pocitace(pole):
    # Podle strategie (funkce strategie_vitezstvi() nebo strategie_obrana()) nebo nahodne zvoli policko pocitace a umisti jej pomoci funkce tah().
    while True:
        if strategie_vitezstvi(pole) != "nic":
            policko = strategie_vitezstvi(pole)
            return util.tah(pole, policko, symbol = "o")
        elif strategie_obrana(pole) != "nic":
            policko = strategie_obrana(pole)
            return util.tah(pole, policko, symbol = "o")
        else:
            policko = randrange(0,19)
            if pole[policko] == "-":
                return util.tah(pole, policko, symbol = "o")

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
