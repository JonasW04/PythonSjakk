import Sjakkbrett as Sjakk
import Sjakkbrikke

def sjekkSjakk():
    pass

def sjekkSjakkMatt():
    pass

def main():
    brett = Sjakk.Sjakkbrett()
    brett.printBrett()
    brett.brikker[8].flytt((6,0))
    print("---------------")
    brett.printBrett()
    
main()