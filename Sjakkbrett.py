import math
import Sjakkbrikke

VANLIGE_STARTPOSISJONER = "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"

class Sjakkbrett():
    brettMatrise = []
    brikker = []
    
    def __init__(self, posisjoner = VANLIGE_STARTPOSISJONER):
            #posisjoner må være en string med lengde som er kvadrattall ettersom sjakkbrett er kvadrater
            self.brettstørrelse = int(math.sqrt(len(posisjoner)))
            self.brettMatrise = [["." for _ in range(self.brettstørrelse)] for _ in range(self.brettstørrelse)] #Lager tomt brett
            
            #Lager brikker og legger dem til i lista brikker som tilhører instansen
            for i, char in enumerate(posisjoner):
                posisjon = (i//self.brettstørrelse, i % self.brettstørrelse)
                x = posisjon[0]
                y = posisjon[1]

                if char.lower() == "p":
                    if char.isupper():
                        brikke = Sjakkbrikke.Bonde(Sjakkbrikke.Farge.HVIT, posisjon, self)
                    else:
                        brikke = Sjakkbrikke.Bonde(Sjakkbrikke.Farge.SVART, posisjon, self)
                    self.brikker.append(brikke)
                    self.brettMatrise[x][y] = brikke

                elif char.lower() == "k":
                    if char.isupper():
                        brikke = Sjakkbrikke.Konge(Sjakkbrikke.Farge.HVIT, posisjon, self)
                    else:
                        brikke = Sjakkbrikke.Konge(Sjakkbrikke.Farge.SVART, posisjon, self)
                    self.brikker.append(brikke)
                    self.brettMatrise[x][y] = brikke

                elif char.lower() == "q":
                    if char.isupper():
                        brikke = Sjakkbrikke.Dronning(Sjakkbrikke.Farge.HVIT, posisjon, self)
                    else:
                        brikke = Sjakkbrikke.Dronning(Sjakkbrikke.Farge.SVART, posisjon, self)
                    self.brikker.append(brikke)
                    self.brettMatrise[x][y] = brikke

                elif char.lower() == "r":
                    if char.isupper():
                        brikke = Sjakkbrikke.Tårn(Sjakkbrikke.Farge.HVIT, posisjon, self)
                    else:
                        brikke = Sjakkbrikke.Tårn(Sjakkbrikke.Farge.SVART, posisjon, self)
                    self.brikker.append(brikke)
                    self.brettMatrise[x][y] = brikke

                elif char.lower() == "n":
                    if char.isupper():
                        brikke = Sjakkbrikke.Springer(Sjakkbrikke.Farge.HVIT, posisjon, self)
                    else:
                        brikke = Sjakkbrikke.Springer(Sjakkbrikke.Farge.SVART, posisjon, self)
                    self.brikker.append(brikke)
                    self.brettMatrise[x][y] = brikke

                elif char.lower() == "b":
                    if char.isupper():
                        brikke = Sjakkbrikke.Løper(Sjakkbrikke.Farge.HVIT, posisjon, self)
                    else:
                        brikke = Sjakkbrikke.Løper(Sjakkbrikke.Farge.SVART, posisjon, self)
                    self.brikker.append(brikke)
                    self.brettMatrise[x][y] = brikke

    def printBrett(self):
        for rad in self.brettMatrise:
            for obj in rad:
                if issubclass(obj.__class__, Sjakkbrikke.Sjakkbrikke):
                    print(obj.symbol, end = "")
                else:
                    print(".", end = "")
            print("")


