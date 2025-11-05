from enum import Enum
import Sjakkbrett

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

class Sjakkbrikke():
    def __init__(self, farge, type, posisjon, symbol, brett):
        self.farge = farge
        self.type = type
        self.posisjon = posisjon
        self.symbol = symbol
        self.brett = brett
        self.x_pos = posisjon[0]
        self.y_pos = posisjon[1]

    def flytt(self, trekk):
        trekk_x = trekk[0]
        trekk_y = trekk[1]
        obj = self.brett.brettMatrise[trekk_x][trekk_y]
        if issubclass(obj.__class__, Sjakkbrikke): #Sletter brikke om den blir slått ut
            obj.slettBrikke()
        self.brett.brettMatrise[self.x_pos][self.y_pos] = "."
        self.brett.brettMatrise[trekk_x][trekk_y] = self
        self.posisjon = trekk

    def slettBrikke(self):
        self.brett.brikker.remove(self)
        del self

    def sjekkMuligeTrekk(brett):
        pass


class Bonde(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♟"
        else:
            symbol = "♙"
        super().__init__(farge, Brikke.BONDE, posisjon, symbol, brett)


class Løper(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♝"
        else:
            symbol = "♗" 
        super().__init__(farge, Brikke.LØPER, posisjon, symbol, brett)


class Tårn(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♜"
        else:
            symbol = "♖"
        super().__init__(farge, Brikke.TÅRN, posisjon, symbol, brett)


class Springer(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♞"
        else:
            symbol = "♘"
        super().__init__(farge, Brikke.SPRINGER, posisjon, symbol, brett)


class Dronning(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♛"
        else:
            symbol = "♕"
        super().__init__(farge, Brikke.DRONNING, posisjon, symbol, brett)


class Konge(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♚"
        else:
            symbol = "♔"
        super().__init__(farge, Brikke.KONGE, posisjon, symbol, brett)


