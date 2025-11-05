from enum import Enum

#Test
class Sjakkbrikke():
    def __init__(self, farge, type, posisjon):
        self.farge = farge
        self.type = type
        self.posisjon = posisjon

    def flytt(trekk):
        pass

    def sjekkMuligeTrekk(brett):
        pass


class Bonde(Sjakkbrikke):
    def __init__(self, farge):
        super().__init__(farge, Brikke.BONDE)


class Løper(Sjakkbrikke):
    def __init__(self, farge):
        super().__init__(farge, Brikke.LØPER)


class Tårn(Sjakkbrikke):
    def __init__(self, farge):
        super().__init__(farge, Brikke.TÅRN)


class Springer(Sjakkbrikke):
    def __init__(self, farge):
        super().__init__(farge, Brikke.SPRINGER)


class Dronning(Sjakkbrikke):
    def __init__(self, farge):
        super().__init__(farge, Brikke.DRONNING)


class Konge(Sjakkbrikke):
    def __init__(self, farge):
        super().__init__(farge, Brikke.KONGE)


class Farge(Enum):
    HVIT = 1
    SVART = 0

class Brikke(Enum):
    BONDE = 0
    LØPER = 1
    TÅRN = 2
    SPRINGER = 3
    DRONNING = 4
    KONGE = 5