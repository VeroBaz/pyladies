import piskvorky
import ai

def test_vyhodnot_x():
    pole = "--xxx---------------"
    assert piskvorky.vyhodnot(pole) == "x"

def test_vyhodnot_continue():
    pole = "---x-o-x---oo-xx----"
    assert piskvorky.vyhodnot(pole) == "-"

def test_strategie_ai_vitezstvi_1():
    pole = ai.tah_pocitace("----x--xo-o---------")
    assert pole.find("ooo") == 8

def test_strategie_ai_vitezstvi_2():
    pole = "--------------------"
    assert ai.strategie_vitezstvi(pole) == "nic"

def test_strategie_ai_obrana_1():
    pole = ai.tah_pocitace("----x--xo--o--------")
    assert pole[3] == "o"

def test_strategie_ai_obrana_2():
    pole = "--------------------"
    assert ai.strategie_obrana(pole) == "nic"

def test_tah_na_prazdne_pole():
    pole = ai.tah_pocitace("--------------------")
    assert len(pole) == 20
    assert pole.count("o") == 1
    assert pole.count("-") == 19
