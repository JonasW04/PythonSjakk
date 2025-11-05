from enum import Enum
import Sjakkbrett

class Sjakkbrikke():
    def __init__(self, farge, type, posisjon, symbol):
        self.farge = farge
        self.type = type
        self.posisjon = posisjon
        self.symbol = symbol

    def flytt(self, trekk):
        self.posisjon = trekk

    def sjekkMuligeTrekk(brett):
        pass


class Bonde(Sjakkbrikke):
    def __init__(self, farge, posisjon):
        if farge == Farge.HVIT:
            symbol = "♟"
        else:
            symbol = "♙"
        super().__init__(farge, Brikke.BONDE, posisjon, symbol)


class Løper(Sjakkbrikke):
    def __init__(self, farge, posisjon):
        if farge == Farge.HVIT:
            symbol = "♝"
        else:
            symbol = "♗" 
        super().__init__(farge, Brikke.LØPER, posisjon, symbol)


class Tårn(Sjakkbrikke):
    def __init__(self, farge, posisjon):
        if farge == Farge.HVIT:
            symbol = "♜"
        else:
            symbol = "♖"
        super().__init__(farge, Brikke.TÅRN, posisjon, symbol)


class Springer(Sjakkbrikke):
    def __init__(self, farge, posisjon):
        if farge == Farge.HVIT:
            symbol = "♞"
        else:
            symbol = "♘"
        super().__init__(farge, Brikke.SPRINGER, posisjon, symbol)


class Dronning(Sjakkbrikke):
    def __init__(self, farge, posisjon):
        if farge == Farge.HVIT:
            symbol = "♛"
        else:
            symbol = "♕"
        super().__init__(farge, Brikke.DRONNING, posisjon, symbol)


class Konge(Sjakkbrikke):
    def __init__(self, farge, posisjon):
        if farge == Farge.HVIT:
            symbol = "♚"
        else:
            symbol = "♔"
        super().__init__(farge, Brikke.KONGE, posisjon, symbol)


class Farge(Enum):
    HVIT = 1
    SVART = 0

class Brikke(Enum):
    BONDE = "P"
    LØPER = "B"
    TÅRN = "R"
    SPRINGER = "N"
    DRONNING = "Q"
    KONGE = "K"