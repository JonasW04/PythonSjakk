import Sjakkbrett as Sjakk
import Sjakkbrikke

def sjekkSjakk():
    pass

def sjekkSjakkMatt():
    pass

def main():
    brett = Sjakk.Sjakkbrett()
    brett.brettMatrise[1][1].flytt((2,1))
    brett.printBrett()
    print(brett.brettMatrise[1][0].trekkErLovlig((2,1)))
    
main()