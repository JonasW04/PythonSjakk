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
        self.x_pos = posisjon[1]
        self.y_pos = posisjon[0]
        self.i_start_posisjon = True
        self.bevegelsesretning = -1 if self.farge == Farge.HVIT else 1

    def flytt(self, trekk):
        trekk_x = trekk[1]
        trekk_y = trekk[0]
        obj = self.brett.brettMatrise[trekk_y][trekk_x]
        if issubclass(obj.__class__, Sjakkbrikke): #Sletter brikke om den blir slått ut
            obj.slettBrikke()
        self.brett.brettMatrise[self.y_pos][self.x_pos] = "."
        self.brett.brettMatrise[trekk_y][trekk_x] = self
        self.posisjon = trekk
        self.i_start_posisjon = False

    def slettBrikke(self):
        self.brett.brikker.remove(self)
        del self

    def trekkErLovlig(brett, trekk):
        pass


class Bonde(Sjakkbrikke):
    def __init__(self, farge, posisjon, brett):
        if farge == Farge.HVIT:
            symbol = "♟"
        else:
            symbol = "♙"
        super().__init__(farge, Brikke.BONDE, posisjon, symbol, brett)

    def trekkErLovlig(self, trekk):
        if trekk == (self.y_pos + self.bevegelsesretning, self.x_pos) and self.brett.brettMatrise[trekk[0]][trekk[1]] == ".":
            return True
        elif  self.i_start_posisjon and trekk == (self.y_pos + 2*self.bevegelsesretning, self.x_pos) and self.brett.brettMatrise[trekk[0]][trekk[1]] == "." and self.brett.brettMatrise[trekk[0] - self.bevegelsesretning][trekk[1]] == ".":
            return True
        elif trekk == (self.y_pos + self.bevegelsesretning, self.x_pos + 1) and self.brett.brettMatrise[trekk[0]][trekk[1]] != "." and self.brett.brettMatrise[trekk[0]][trekk[1]].farge != self.farge:
            return True
        elif trekk == (self.y_pos + self.bevegelsesretning, self.x_pos - 1) and self.brett.brettMatrise[trekk[0]][trekk[1]] != "." and self.brett.brettMatrise[trekk[0]][trekk[1]].farge != self.farge:
            return True
        return False
            
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


