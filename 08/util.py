# Cast hry piskvorky - provadi tah

def tah(pole, policko, symbol):
    # Umistuje symbol hrace na zvolene policko v hernim poli.
    pole = "".join(list(pole)[:policko]) + symbol + "".join(list(pole)[policko + 1:])
    return pole